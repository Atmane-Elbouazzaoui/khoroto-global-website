// The public invitation contract mirrors Piccolo Squad's PartyInviteLink fields.
// A syntactically valid link is not proof that a Photon room is still available.
export const ORIGIN = 'https://khorotoglobal.com';
export const ANDROID_PACKAGE = 'com.piccolosquad.online.coop.party.puzzle';
const required = ['code', 'region', 'version', 'room'];
const allowed = new Set([...required, 'cluster']);
const patterns = {
  code: /^[A-Z0-9]{6}$/,
  region: /^[a-z]{2,8}$/,
  version: /^[A-Za-z0-9._-]{1,32}$/,
  room: /^[a-fA-F0-9]{32}$/,
  cluster: /^[A-Za-z0-9._-]{1,32}$/,
};

export function parseInvitation(search, hash = '') {
  if (typeof search !== 'string' || !search || search === '?' || search.length > 2048 || hash) return null;
  const raw = search.startsWith('?') ? search.slice(1) : search;
  if (raw.split('&').some(pair => pair.indexOf('=') <= 0 || pair.endsWith('='))) return null;
  const query = new URLSearchParams(search);
  const entries = [...query];
  if (entries.length < 4 || entries.length > 5) return null;
  const seen = new Set();
  for (const [key, value] of entries) {
    // Comparing the complete match also rejects a trailing line terminator;
    // JavaScript's $ anchor alone can match just before that final character.
    if (!allowed.has(key) || seen.has(key) || patterns[key].exec(value)?.[0] !== value) return null;
    seen.add(key);
  }
  if (!required.every(key => seen.has(key))) return null;
  return Object.fromEntries(entries);
}

export function invitationUrl(invitation) {
  const query = new URLSearchParams(required.map(key => [key, invitation?.[key] ?? '']));
  if (invitation?.cluster != null) query.set('cluster', invitation.cluster);
  if (!parseInvitation(query.toString())) throw new TypeError('Invalid invitation');
  return `${ORIGIN}/party/?${query}`;
}

export function androidIntent(invitation) {
  const url = invitationUrl(invitation);
  const fallback = encodeURIComponent(`${ORIGIN}/piccolo-squad.html#availability`);
  return `intent://${url.slice('https://'.length)}#Intent;scheme=https;package=${ANDROID_PACKAGE};S.browser_fallback_url=${fallback};end`;
}
