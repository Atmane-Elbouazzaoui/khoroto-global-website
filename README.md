# Khoroto Global

Static GitHub Pages website for **Khoroto Global**, publishing **Piccolo Squad**
and **Brainrot Bills: Smash Egg ASMR** on Android. Public contact:
support@khorotoglobal.xyz. The responsible publisher, **Radi Akka**, is identified
in the privacy, terms and account-deletion information. Promotional pages,
shared footers and page metadata use the publishing brand.

Canonical domain: **https://khorotoglobal.xyz**.

The visual theme and page structure follow the existing Alulim studio website,
with the owner-supplied Khoroto emblem and current game artwork. Existing sites
and iOS releases are separate and remain unchanged.

## Build and check

No third-party runtime or build dependencies are needed. Python 3 and Node.js
provide the renderer and invitation checks:

```sh
python3 scripts/build_site.py
python3 scripts/check_site.py
node --test scripts/invitation.test.mjs
python3 scripts/prepare_pages.py
python3 -m http.server 8765 --directory dist --bind 127.0.0.1
```

Open http://127.0.0.1:8765 for local review. `dist/` is the checked artifact;
`docs/` is its generated copy for branch-based GitHub Pages publishing. Edit body
content in `content/`, shared markup in `scripts/build_site.py`, and additions
to the preserved theme in `css/khoroto.css`.

On macOS, generated copies use independent copy-on-write clones when supported,
avoiding duplicate image storage. Other filesystems use ordinary file copies.
The gallery includes eight phone/tablet screenshot pairs and both supplied
feature-graphic sizes. Their original filenames and hashes are recorded in
`notes/PICCOLO_GALLERY_ASSETS.json`; the PNGs are copied without image edits.

The homepage features both games in a manual native-scroll carousel. Its only
JavaScript is a 657-byte click handler for the game-selection buttons: no autoplay,
timers, observers, animation loop or third-party carousel dependency. The game
catalogue uses a large tablet screenshot with two smaller Piccolo views and two
stacked Brainrot gameplay screenshots. CSS animation/transition and header blur
are disabled; screenshots below the hero load lazily.

## Pages

The site contains the studio home, two game pages, game-policy directory,
separate Android privacy policies, game terms, support and ad/bug-report
instructions, account/data deletion instructions, website privacy, provider
directory, credits/notices, party landing page, and 404 page.

The party page validates all connection fields, preserves the room instance and
optional cluster, prepares a user-initiated Android intent, and offers sharing
and clipboard fallbacks. It does not verify live room availability, auto-open
an app, redirect to an Apple store, or send invitation data to an API.

## Publication and remaining service setup

- Publish from `main`, folder `/docs`, using standard GitHub Pages branch
  publishing. `prepare_pages.py` builds, checks, tests, and prepares those files.
  Its `--preview` option omits CNAME until the domain is ready. Normal production
  preparation includes CNAME.
- An optional Actions workflow is saved under `config/`; it is not active. The
  current GitHub credential cannot create workflow files, so branch publishing
  avoids a request for expanded credential scope.
- The custom domain, Namecheap DNS and enforced HTTPS are configured and verified.
  Keep the production CNAME when preparing updates. See
  [publication notes](notes/PUBLICATION.md).
- Ad-seller authorization is explicitly deferred by the owner to the next update.
  No seller IDs
  from another site are silently authorized here. Add the verified provider
  export as `config/app-ads.verified.txt` when confirmed; it will be deployed as
  `/app-ads.txt` on the next build.
- The Android association is configured for the verified **direct-install APK**
  signer of Piccolo Squad 2.0 (version code 1), package
  `com.piccolosquad.online.coop.party.puzzle`. `apksigner verify` passed for the
  APK with SHA-256 `98fe06987c5be33667b3a6711a3a8be0aa782dfa8053126eed5080e23fd19d56`.
  `config/assetlinks.verified.json` publishes its certificate fingerprint at
  `/.well-known/assetlinks.json`. The excluded template remains a reference.
  **Play-delivered App Links still need the actual Play app-signing certificate**
  before store release; add its verified fingerprint if it differs. An upload
  certificate is not proof of the Play app-signing certificate. Only public
  fingerprints belong here; private keys and passwords stay outside the site.
- Both agreed Google Play URLs are wired. Brainrot Bills: Smash Egg ASMR returned
  HTTP 200 with its exact title. The owner requested Piccolo Squad's final package
  URL before launch; it returned HTTP 404 at the latest check, so the page asks
  visitors to check availability rather than claiming it is already available.
- Piccolo Squad Android public URLs have migrated after domain verification.
  Legacy invitation parsing, service endpoints and the separate iOS checkout are
  preserved. A physical Android check remains necessary.

The developer identity and Android scope were supplied and confirmed by the
owner. Ad-account authorization remains pending. The developer handles incoming
support/deletion requests. Policies describe the inspected Android source; they
do not establish store acceptance or physical-device behavior.
