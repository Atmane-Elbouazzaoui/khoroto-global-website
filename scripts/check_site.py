#!/usr/bin/env python3
"""Check the deployable artifact, public identities, references and privacy boundaries."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, urljoin, unquote
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'dist'
ORIGIN = 'https://khorotoglobal.xyz'


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.images, self.meta, self.texts = [], [], [], [], []
        self.h1 = 0
        self.title = 0
        self.errors = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.append(a['id'])
        if tag == 'h1':
            self.h1 += 1
        if tag == 'title':
            self.title += 1
        if tag == 'meta':
            self.meta.append(a)
        for key in ['href', 'src']:
            if key in a:
                self.links.append(a[key])
        for candidate in a.get('srcset', '').split(','):
            if candidate.strip():
                self.links.append(candidate.strip().split()[0])
        if tag == 'img':
            self.images.append(a)
        if tag in ['iframe', 'form', 'base']:
            self.errors.append(f'unexpected {tag} element')
        if any(key.startswith('on') for key in a):
            self.errors.append('inline event handler')

    def handle_data(self, value):
        self.texts.append(value)


def check():
    errors = []
    pages = {str(path.relative_to(SITE)): Page(path.read_text()) for path in SITE.rglob('*.html')}
    references = 0
    for name, page in pages.items():
        raw = (SITE / name).read_text()
        visible = ' '.join(page.texts)
        if page.h1 != 1 or page.title != 1:
            errors.append(f'{name}: expected one title and one h1')
        if len(page.ids) != len(set(page.ids)):
            errors.append(f'{name}: duplicate IDs')
        if not any(m.get('name') == 'description' and m.get('content') for m in page.meta):
            errors.append(f'{name}: missing description')
        if 'Khoroto Global' not in visible:
            errors.append(f'{name}: missing publisher brand')
        identity_pages = {'privacy.html', 'brainrot-bills-privacy.html',
                          'website-privacy.html', 'terms.html', 'delete-account.html'}
        if name in identity_pages:
            if visible.count('Radi Akka') != 1:
                errors.append(f'{name}: expected one responsible-publisher identification')
        elif 'Radi Akka' in raw:
            errors.append(f'{name}: personal name outside legal/privacy information')
        if re.search(r'Pippin Plaza|Alulim Games|Atmane El Bouazzaoui', visible, re.I):
            errors.append(f'{name}: old public identity')
        if 'armando.b.higgin@gmail.com' in raw:
            errors.append(f'{name}: superseded public email')
        if 'Smash an Egg' in raw:
            errors.append(f'{name}: superseded Brainrot Bills title')
        if re.search(r'@@[A-Z_]+@@|__VERIFIED_', raw):
            errors.append(f'{name}: unresolved placeholder')
        for image in page.images:
            if 'alt' not in image or not image.get('width') or not image.get('height'):
                errors.append(f'{name}: missing image accessibility/dimensions')
        errors.extend(f'{name}: {error}' for error in page.errors)
        for link in page.links:
            url = urlsplit(urljoin(ORIGIN + '/' + name, link))
            if url.scheme in ['mailto', 'intent']:
                continue
            if url.scheme != 'https':
                errors.append(f'{name}: unsupported link scheme: {link}')
                continue
            if url.netloc != 'khorotoglobal.xyz':
                if url.netloc in ['pippinplaza.com', 'alulimgames.com']:
                    errors.append(f'{name}: old public URL: {link}')
                continue
            target = unquote(url.path).lstrip('/') or 'index.html'
            if target.endswith('/'):
                target += 'index.html'
            if not (SITE / target).is_file():
                errors.append(f'{name}: missing target: {link}')
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f'{name}: missing anchor: {link}')
            references += 1
    if len(pages) != 14:
        errors.append(f'Expected 14 pages, found {len(pages)}')
    expected_listings = {
        'piccolo-squad.html': 'https://play.google.com/store/apps/details?id=com.piccolosquad.online.coop.party.puzzle',
        'brainrot-bills.html': 'https://play.google.com/store/apps/details?id=com.alulimgames.brainrotbills',
    }
    for name, listing in expected_listings.items():
        if listing not in pages[name].links:
            errors.append(f'{name}: missing agreed Google Play destination')
    if 'assets/piccolo-squad-background.png' in pages['index.html'].links:
        errors.append('Homepage still promotes the raw game background')
    carousel = SITE / 'js/home-carousel.mjs'
    if not carousel.is_file() or carousel.stat().st_size > 2048:
        errors.append('Homepage carousel script missing or above its 2 KiB budget')
    elif re.search(r'\b(setInterval|setTimeout|requestAnimationFrame|requestIdleCallback|IntersectionObserver|MutationObserver)\b', carousel.read_text()):
        errors.append('Homepage carousel must stay user-driven without timers or background observers')
    if (SITE / 'CNAME').read_text().strip() != 'khorotoglobal.xyz':
        errors.append('Wrong custom domain')
    if hashlib.sha256((SITE / 'assets/khoroto-logo.png').read_bytes()).hexdigest() != '406c580ea9df593a3b9dc1121242624364c3a9c29cf24a3aacb2957eb29e8b3d':
        errors.append('Supplied logo pixels changed')
    for path in SITE.rglob('*'):
        if path.is_file() and path.suffix in ['.html', '.js', '.mjs']:
            value = path.read_text()
            if re.search(r'localStorage|sessionStorage|document\.cookie|\bfetch\s*\(|XMLHttpRequest', value):
                errors.append(f'{path.name}: unexpected tracking/storage/network API')
    for path in ['scripts', 'content', 'docs', 'config']:
        if (SITE / path).exists():
            errors.append(f'Private source directory leaked into artifact: {path}')
    report = {'pages':len(pages), 'internalReferences':references, 'errors':errors,
              'adSellerAuthorization':'configured' if (SITE/'app-ads.txt').is_file() else 'pending',
              'androidAppLinks':'configured' if (SITE/'.well-known/assetlinks.json').is_file() else 'pending signed-certificate evidence',
              'renderedBrowserQA':'not available; Chrome control not authorized'}
    print(json.dumps(report, indent=2))
    return bool(errors)


if __name__ == '__main__':
    sys.exit(check())
