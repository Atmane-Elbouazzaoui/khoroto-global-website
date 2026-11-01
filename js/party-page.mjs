import { parseInvitation, invitationUrl, androidIntent } from './invitation.mjs';

const invitation = parseInvitation(location.search, location.hash);
const get = id => document.getElementById(id);
if (invitation) {
  get('invitation-placeholder').hidden = true;
  get('invitation-valid').hidden = false;
  get('party-code').textContent = invitation.code;
  get('party-region').textContent = invitation.region.toUpperCase();
  get('party-version').textContent = invitation.version;
  const url = invitationUrl(invitation);
  get('copy-fallback').value = url;
  if (/Android/i.test(navigator.userAgent)) {
    get('open-game').href = androidIntent(invitation);
    get('open-game').hidden = false;
  }
  get('copy-link').addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(url);
      get('party-status').textContent = 'Full invitation link copied.';
    } catch {
      get('copy-fallback-label').hidden = false;
      get('copy-fallback').hidden = false;
      get('copy-fallback').focus();
      get('copy-fallback').select();
      get('party-status').textContent = 'Select and copy the full invitation link below.';
    }
  });
  if (typeof navigator.share === 'function') {
    get('share-link').hidden = false;
    get('share-link').addEventListener('click', async () => {
      try {
        await navigator.share({ title: 'Piccolo Squad party', text: 'Join my Piccolo Squad party.', url });
      } catch (error) {
        if (error?.name !== 'AbortError') get('party-status').textContent = 'Sharing is unavailable here. Use Copy invitation link.';
      }
    });
  }
} else if (location.search || location.hash) {
  get('invitation-placeholder').hidden = true;
  get('invitation-invalid').hidden = false;
}
