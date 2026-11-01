# Khoroto Global

Static GitHub Pages website for **Radi Akka**, an individual game developer based
in Morocco, publishing **Piccolo Squad** and **Brainrot Bills: Smash an Egg** on
Android under **Khoroto Global**. Public contact: armando.b.higgin@gmail.com.

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
python3 scripts/prepare_pages.py --preview
python3 -m http.server 8765 --directory dist --bind 127.0.0.1
```

Open http://127.0.0.1:8765 for local review. `dist/` is the checked artifact;
`docs/` is its generated copy for branch-based GitHub Pages publishing. Edit body
content in `content/`, shared markup in `scripts/build_site.py`, and additions
to the preserved theme in `css/khoroto.css`.

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
- Configure the custom domain in GitHub Pages before pointing DNS to it. The
  generated CNAME documents the intended domain. Configure the same custom domain
  in repository Pages settings when switching from preview to production.
- Add the domain's DNS records and enable HTTPS after GitHub issues its
  certificate. See [publication notes](notes/PUBLICATION.md).
- Ad-seller authorization was explicitly deferred by the owner. No seller IDs
  from another site are silently authorized here. Add the verified provider
  export as `config/app-ads.verified.txt` when confirmed; it will be deployed as
  `/app-ads.txt` on the next build.
- The Android association template is excluded from deployment. Replace its
  placeholder using the actual Play app-signing SHA-256 certificate(s), verify
  package/signature provenance, and save it as `config/assetlinks.verified.json`
  to publish `/.well-known/assetlinks.json`. An upload key is not automatically
  the Play app-signing key. Do not place private keys or passwords here.
- The site does not guess store availability. Add download links only after
  their exact listing and availability are confirmed.
- Migrate Piccolo Squad Android public URLs only after the new domain is
  verified. Keep legacy invitation parsing, service endpoints, and the separate
  iOS checkout intact. A physical Android check remains necessary.

The developer identity and Android scope were supplied and confirmed by the
owner. Ad-account authorization remains pending. The developer handles incoming
support/deletion requests. Policies describe the inspected Android source; they
do not establish store acceptance or physical-device behavior.
