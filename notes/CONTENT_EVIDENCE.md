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
