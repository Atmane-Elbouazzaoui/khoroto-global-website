# Content evidence — 2026-11-01

## Identity and scope

Owner supplied: Khoroto Global; developer given name Akka, family name Radi;
displayed name Radi Akka; individual game developer based in Morocco;
support@khorotoglobal.xyz; khorotoglobal.xyz; supplied Khoroto logo. Confirmed
Android-only coverage for Piccolo Squad and Brainrot Bills. No iOS changes.

On November 1, the owner confirmed that `support@khorotoglobal.xyz` forwards
through Namecheap to their existing Gmail inbox and that a delivery test worked.
This is owner-reported receipt; no email was sent by the agent. The public site
uses the domain address for support, privacy and deletion requests.

The owner later clarified that Radi Akka is the responsible Android publisher,
with the user contributing development. The live iOS release keeps its existing
domain and setup.

The logo copy is byte-identical to the supplied PNG:
`406c580ea9df593a3b9dc1121242624364c3a9c29cf24a3aacb2957eb29e8b3d`.

## Brainrot Bills Android

Read-only source inspection of Project_PiggyLedger_iOS, the Android release lane:

- `Docs/Design/GOOGLE_PLAY_SPEC_2026-10-01.md`, including its reward-hub and
  connection-gate addendum; `Docs/Roadmap/DECISIONS.md` Google Play release entry.
- `Packages/manifest.json`: no Auth, Analytics, Firebase, cloud-save, attribution,
  or IAP package in the inspected Android manifest.
- `Assets/_Project/Content/Catalogs/AdvertisingConfig.asset`: LevelPlay, Android
  interstitial/rewarded IDs, child-directed setting off.
- `InHouseConsentPlatform.cs`, `LevelPlayAdService.cs`, `ConsentCopy.cs`, and
  `SettingsPresenter.cs`: privacy-choice persistence, consent applied before ad
  initialization, and reward-confirmation callbacks.

Corrections to the owner-supplied policy sample: narrow it to this Android game;
do not extend an offline/local-save policy to Piccolo; remove unverified banner
claims; describe interstitials between runs and optional rewarded ads; distinguish
local saves from the Android internet requirement; use the new policy date rather
than backdate a changed policy to October 15.

## Piccolo Squad Android

### Store destinations and supplied screenshots

The owner confirmed the published Android title **Brainrot Bills: Smash Egg ASMR**
and listing `https://play.google.com/store/apps/details?id=com.alulimgames.brainrotbills`.
A read-only HTTP check returned 200 and found that exact title in the response.
The old full title has been replaced in page metadata, game copy and policy scope.

The owner requested the final Piccolo Squad destination now:
`https://play.google.com/store/apps/details?id=com.piccolosquad.online.coop.party.puzzle`.
It returned HTTP 404 at the check on November 1; the page links to it with neutral
availability wording. This is not evidence of a live Piccolo listing. Neither
game page automatically redirects to a store, and no Apple destination was added.

The supplied `Poogle Play Store Assets` folder contains the feature graphics and
phone/tablet PNGs used in the Piccolo gallery. Eight screenshot pairs and two
feature sizes were copied byte-for-byte. Full original filenames, dimensions,
sizes and SHA-256 hashes are in `PICCOLO_GALLERY_ASSETS.json`. Each gallery card
offers both full-size originals; responsive images retain their natural aspect
ratio without cropping. The user corrected the painted Flappy Piccolo wording
in phone images 03/06 and tablet image 06. Fresh visual inspection confirmed the
corrections, including the explicitly identified `06_Solo52_Flap_Switch_2752x2064.png`.

Local verification: all 18 originals match source, generated and Pages copies
(72 hash/dimension comparisons); all 52 public files match between dist and docs;
14 pages, 537 internal references and all five invitation test groups pass.
Rendered desktop/mobile review remains the owner's next check. Chrome was not
controlled. On this Mac, independent APFS clones avoid extra physical image copies
after ordinary copies encountered an actual disk-full error; portable ordinary
copy fallback is retained. Original images were not changed by the agent.

Read-only source inspection of Pippin_Piccolo_Android:

- `Packages/manifest.json`, `SocialConfiguration.asset`, `ConsentManager.cs`,
  `AnalyticsLogger.cs`, `SocialAccountPanel.cs`, `SocialNotificationsPanel.cs`.
- `EconomyFrontendProductionBinding.cs`: Android local ads-funded wallet and no
  billing bootstrap; iOS commerce terms must not be copied into Android policy.
- Social Worker `worker.mjs`, `profiles.mjs`, `social-policy.mjs`, `tickets.mjs`,
  `reports.mjs`, `deliveries.mjs`: names/IDs, friends/presence, tokens, invitation
  expiry and deletion. Report cleanup is request-triggered, not a guaranteed
  scheduled 30-day physical deletion. A deleted-account hash denies still-valid
  tokens for 3660 seconds, then is eligible for request-triggered cleanup.
- `PartyInviteLink.cs`: exact code, region, room, version, cluster contract.
- Existing legal pages were references, not proof that iOS commerce behavior
  applies to Android.

Primary provider/policy references reviewed:

- https://unity.com/legal/game-player-and-app-user-privacy-policy
- https://firebase.google.com/support/privacy
- https://www.photonengine.com/terms/privacyandcookiepolicy
- https://www.cloudflare.com/privacypolicy/
- https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement
- https://support.google.com/googleplay/android-developer/answer/13327111
- https://developer.chrome.com/docs/android/intents

## Regression review

- Critical: no gameplay, saves, networking authority, economy, or iOS changes
  are part of the website build.
- High: original websites and user artwork remain unchanged; no credential or
  private signing material is added; incomplete ad/signature configuration is
  excluded from the deployed artifact.
- Mid: strict invitation validation, full-field round trips, safe Android
  destination/fallback, invalid-link handling, clipboard fallback, complete
  internal-link/anchor checks. Live room and device behavior remain separate.
- Low: shared responsive theme, local fonts/images, semantic headings and labels,
  reduced-motion support. Rendered review is pending because only Chrome is
  connected and Chrome control has not been authorized.
