#!/usr/bin/env python3
"""Render a portable static site using only Python's standard library."""
from pathlib import Path
from html import escape
import json
import re
import shutil
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dist"
ORIGIN = "https://khorotoglobal.xyz"
EMAIL = "armando.b.higgin@gmail.com"


def brand(prefix):
    return f'''<a class="brand" href="{prefix}index.html" aria-label="Khoroto Global home">
      <img class="brand-mark" src="{prefix}assets/khoroto-logo.png" alt="" width="885" height="885">
      <span class="brand-name" aria-hidden="true"><span class="brand-name-primary">Khoroto</span><span class="brand-name-secondary">Global</span></span></a>'''


def navigation(prefix):
    links = f'''<a href="{prefix}index.html#games">Games</a><a href="{prefix}index.html#studio">Studio</a><a href="{prefix}support.html">Support</a>'''
    return f'''<header class="site-header"><div class="shell nav-shell">{brand(prefix)}
      <nav class="site-nav" aria-label="Primary navigation">{links}</nav>
      <a class="header-contact" href="{prefix}support.html#contact">Contact</a>
      <details class="mobile-nav"><summary aria-label="Navigation menu"><span class="menu-icon" aria-hidden="true"></span></summary>
      <nav class="mobile-panel" aria-label="Mobile navigation">{links}<a href="{prefix}policies.html">Game policies</a><a href="{prefix}support.html#contact">Contact</a></nav></details>
    </div></header>'''


def footer(prefix):
    return f'''<footer class="site-footer"><div class="shell"><div class="footer-grid"><div>{brand(prefix)}
      <p class="footer-intro">Play together. Make a little chaos. Find your next good game.</p>
      <p class="footer-intro">Khoroto Global is the publishing brand of <strong>Radi Akka</strong>, an individual game developer based in Morocco.</p></div>
      <div class="footer-group"><h2>Explore</h2><nav aria-label="Footer games"><a href="{prefix}piccolo-squad.html">Piccolo Squad</a><a href="{prefix}brainrot-bills.html">Brainrot Bills</a><a href="{prefix}support.html">Support & contact</a></nav></div>
      <div class="footer-group"><h2>Player information</h2><nav aria-label="Footer legal"><a href="{prefix}policies.html">Game policies</a><a href="{prefix}delete-account.html">Account & data deletion</a><a href="{prefix}licenses.html">Licenses & credits</a><a href="{prefix}website-privacy.html">Website privacy</a></nav></div></div>
      <div class="footer-bottom"><p>&copy; 2026 Radi Akka · Khoroto Global.</p><p>Independent games / Made in Morocco</p></div></div></footer>'''


def render(page):
    path = page["path"]
    prefix = "../" * (len(Path(path).parts) - 1)
    if path == "404.html":
        prefix = "/"  # A 404 may be rendered at an arbitrarily deep request path.
    body = (ROOT / "content" / page["body"]).read_text().replace("@@ROOT@@", prefix)
    if page.get("document"):
        sections = re.findall(r'<h2 id="([a-z0-9-]+)">(.*?)</h2>', body)
        toc = "".join(f'<a href="#{key}">{re.sub("<[^>]+>", "", title)}</a>' for key, title in sections)
        body = f'''<section class="page-hero"><div class="shell"><span class="eyebrow">{escape(page['eyebrow'])}</span><h1>{escape(page['heading'])}</h1><p>{escape(page['description'])}</p></div></section>
          <section class="section document-section"><div class="shell document-grid"><aside class="document-index"><h2>On this page</h2><nav aria-label="Document contents">{toc}</nav><a class="detail-link" href="{prefix}policies.html">All game policies</a></aside><article class="prose">{body}</article></div></section>'''
    canonical_path = "/" if path == "index.html" else "/party/" if path == "party/index.html" else "/" + path
    canonical = ORIGIN + canonical_path
    picture = page.get("image", "assets/khoroto-logo.png")
    title, description = escape(page["title"], quote=True), escape(page["description"], quote=True)
    robots = '<meta name="robots" content="noindex, nofollow">' if page.get("noindex") else ""
    script = f'<script type="module" src="{prefix}{page["script"]}"></script>' if page.get("script") else ""
    return f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><meta name="description" content="{description}"><meta name="author" content="Radi Akka">
<meta name="theme-color" content="#f3eee4"><meta name="referrer" content="no-referrer">{robots}
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; font-src 'self'; connect-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'">
<meta property="og:type" content="website"><meta property="og:site_name" content="Khoroto Global"><meta property="og:url" content="{canonical}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{description}"><meta property="og:image" content="{ORIGIN}/{picture}"><meta property="og:image:alt" content="Khoroto Global — games by Radi Akka">
<meta name="twitter:card" content="summary_large_image"><link rel="canonical" href="{canonical}">
<link rel="icon" type="image/png" href="{prefix}assets/khoroto-logo.png" sizes="885x885"><link rel="manifest" href="{prefix}site.webmanifest">
<link rel="stylesheet" href="{prefix}css/style.css"><link rel="stylesheet" href="{prefix}css/khoroto.css">
</head><body><a class="skip-link" href="#main">Skip to content</a>{navigation(prefix)}<main id="main">{body}</main>{footer(prefix)}{script}</body></html>
'''


def build():
    OUTPUT.mkdir(exist_ok=True)
    pages = json.loads((ROOT / "content/pages.json").read_text())
    for folder in ["assets", "css", "js"]:
        shutil.copytree(ROOT / folder, OUTPUT / folder, dirs_exist_ok=True)
    for page in pages:
        target = OUTPUT / page["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render(page))
    (OUTPUT / ".nojekyll").touch()
    (OUTPUT / "CNAME").write_text("khorotoglobal.xyz\n")
    (OUTPUT / "site.webmanifest").write_text(json.dumps({"name":"Khoroto Global", "short_name":"Khoroto", "start_url":"./", "scope":"./", "display":"browser", "theme_color":"#f3eee4", "background_color":"#f3eee4", "icons":[{"src":"assets/khoroto-logo.png", "sizes":"885x885", "type":"image/png", "purpose":"any"}]}, indent=2) + "\n")
    (OUTPUT / "robots.txt").write_text("User-agent: *\nAllow: /\nDisallow: /party/\nSitemap: " + ORIGIN + "/sitemap.xml\n")
    ET.register_namespace("", "http://www.sitemaps.org/schemas/sitemap/0.9")
    sitemap = ET.Element("{http://www.sitemaps.org/schemas/sitemap/0.9}urlset")
    for page in pages:
        if not page.get("noindex"):
            entry = ET.SubElement(sitemap, "url")
            ET.SubElement(entry, "loc").text = ORIGIN + ("/" if page["path"] == "index.html" else "/" + page["path"])
    ET.ElementTree(sitemap).write(OUTPUT / "sitemap.xml", encoding="utf-8", xml_declaration=True)
    # These files are deployed only once actual seller IDs and signing certificates
    # have been verified. Drafts and placeholders never enter the public artifact.
    for source_name, destination in [("config/app-ads.verified.txt", "app-ads.txt"), ("config/assetlinks.verified.json", ".well-known/assetlinks.json")]:
        source = ROOT / source_name
        target = OUTPUT / destination
        if source.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        elif target.exists():
            target.unlink()
    print(f"Rendered {len(pages)} pages into {OUTPUT}")


if __name__ == "__main__":
    build()
