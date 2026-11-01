# Publication notes — 2026-11-01

Owner-confirmed scope: both Android games; GitHub repository
`Atmane-Elbouazzaoui/khoroto-global-website`; migrate Piccolo Android public links
after new-site verification; preserve old invitation compatibility. Ad-seller
authorization is deliberately pending. Existing sites and iOS stay unchanged.

The owner selected **khorotoglobal.xyz** after reviewing the first-year and renewal
prices and confirmed purchase on Namecheap using BasicDNS. The owner will perform
the website visual check. DNS and HTTPS are verified, and HTTPS is enforced.
The owner configured Namecheap forwarding for `support@khorotoglobal.xyz` to
their existing Gmail inbox and confirmed a successful delivery test.

The support-address publication is commit `d408833f9c97536df5fef10ce383780662a8c1fd`,
Pages run `41266089273` (success). GitHub's certificate restart generated CNAME
commits `fc6dd3e` and `316b888`; the resulting domain remains `khorotoglobal.xyz`.
All 34 public files returned HTTPS 200 and matched their prepared source bytes.
`www` redirects to the apex, and HTTP redirects to HTTPS. The local operational
report is `notes/verification-live.json` (ignored).

The owner chose to verify only the new Android host and preserve old invitations
through in-game paste parsing. Existing sites and Apple associations remain
unchanged. Android device verification awaits the actual signed build certificate.

## Screenshot and store-link update

The current update adds the owner-supplied feature graphics and eight paired
phone/tablet screenshots to Piccolo Squad, including the corrected Flappy Piccolo
images. It wires both final Google Play destinations and uses the full published
Brainrot Bills title **Brainrot Bills: Smash Egg ASMR**. Piccolo's listing is
prewired by owner request with availability wording; it returned 404 at the
November 1 check. The Brainrot listing returned 200 with its exact supplied title.

Local preparation passes for 14 pages, 537 internal references, five invitation
test groups and 52 public files. All 18 supplied PNGs match their manifest hashes
in source and both generated copies. The original downloads remain unchanged.
The live deployment report is saved locally as
`notes/verification-gallery-live.json`; a successful HTTP/hash report still does
not establish desktop/mobile appearance. The owner will review after restarting
macOS. No Chrome session was controlled.

## Hosting

Source is published from `main:/docs` using standard GitHub Pages branch
publishing. The owner-confirmed account credential lacks workflow-write scope;
the initial Actions push was rejected. No ref was published by that rejected
push. The optional workflow is kept outside `.github/workflows`.

## Custom domain

GitHub's current guidance is to verify the domain for the owning account, add
the custom domain in repository Pages settings, then configure DNS. For an apex
domain, use these A records for `@`:

```text
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

For `www`, use a CNAME to `atmane-elbouazzaoui.github.io` (no repository suffix).
Once certificates are available, enforce HTTPS. Account-domain verification
requires GitHub's actual TXT challenge; no challenge value is invented here.
DNS and certificate changes may take time to propagate.

Official references:

- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages
- https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages

## Gates kept separate

Source/build/link checks; rendered desktop/mobile review; GitHub deployment;
custom-domain DNS and HTTPS; ad-seller authorization; Android signing and App
Links; app URL cutover; physical Android acceptance; store release.

The owner reported the Unity Play Mode artwork check passed on 2026-11-01. That
report covers the game visual check, not the website or native Android checks.
