# Publication notes — 2026-11-01

Owner-confirmed scope: both Android games; GitHub repository
`Atmane-Elbouazzaoui/khoroto-global-website`; migrate Piccolo Android public links
after new-site verification; preserve old invitation compatibility. Ad-seller
authorization is deliberately pending. Existing sites and iOS stay unchanged.

The owner selected **khorotoglobal.xyz** after reviewing the first-year and renewal
prices and confirmed purchase on Namecheap using BasicDNS. The owner will perform
the website visual check. The production CNAME is prepared; DNS setup and the
custom-domain certificate still need verification.

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
