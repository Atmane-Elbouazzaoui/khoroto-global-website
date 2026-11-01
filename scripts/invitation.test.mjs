import test from 'node:test';
import assert from 'node:assert/strict';
import { parseInvitation, invitationUrl, androidIntent } from '../js/invitation.mjs';

const example = { code: 'AB12C3', region: 'eu', version: 'untimed-v4-ads', room: '0123456789abcdef0123456789abcdef' };
const query = value => new URLSearchParams(value).toString();

test('preserves every connection field through a share round trip', () => {
  for (const data of [example, { ...example, cluster: 'eu-2.a_1' }]) {
    const url = new URL(invitationUrl(data));
    assert.equal(url.origin, 'https://khorotoglobal.com');
    assert.equal(url.pathname, '/party/');
    assert.deepEqual(parseInvitation(url.search), data);
  }
});

test('rejects missing, duplicate and unknown fields instead of dropping them', () => {
  for (const key of Object.keys(example)) {
    const incomplete = { ...example }; delete incomplete[key];
    assert.equal(parseInvitation(query(incomplete)), null);
  }
  for (const suffix of ['&', '&&', '&cluster', '&cluster=', '&code=ZZZZZZ', '&region=us', '&room='+example.room, '&cluster=a&cluster=b', '&redirect=https://evil.example', '&Code=AB12C3']) {
    assert.equal(parseInvitation(query(example) + suffix), null);
  }
});

test('rejects malformed, overlong and injection-shaped field values', () => {
  const bad = {
    code: ['abcdef', 'AB12C', 'AB12C34', '<img/>', 'ＡB12C3', 'AB12 C', 'AB12C3\n', 'AB12C3\r', 'AB12C3\u2028', 'AB12C3\u2029'],
    region: ['e', 'EU', 'europeeee', 'eu/'],
    version: ['', 'a'.repeat(33), 'v;end', 'v#Intent', '<script>'],
    room: ['', example.room+'0', 'g'.repeat(32), 'javascript:alert(1)'],
    cluster: ['', 'a'.repeat(33), 'eu;end', '../x/'],
  };
  for (const [key, values] of Object.entries(bad)) {
    for (const value of values) assert.equal(parseInvitation(query({ ...example, [key]: value })), null, `${key}: ${value}`);
  }
  assert.equal(parseInvitation(query(example), '#x'), null);
  assert.equal(parseInvitation('?'+'a'.repeat(2049)), null);
  assert.equal(parseInvitation('?'), null);
  assert.equal(parseInvitation(null), null);
});

test('decoded duplicate keys and percent-encoded injection cannot bypass validation', () => {
  assert.equal(parseInvitation(query(example)+'&%63ode=AAAAAA'), null);
  assert.equal(parseInvitation(query(example).replace('AB12C3', '%3Csvg%3E')), null);
  assert.equal(parseInvitation(query(example).replace('AB12C3', 'AB%00C3')), null);
});

test('Android intent pins the destination package, host and safe fallback', () => {
  const intent = androidIntent({ ...example, cluster:'us-1' });
  assert.ok(intent.startsWith('intent://khorotoglobal.com/party/?'));
  assert.ok(intent.includes(';package=com.piccolosquad.online.coop.party.puzzle;'));
  assert.ok(intent.includes('S.browser_fallback_url='+encodeURIComponent('https://khorotoglobal.com/piccolo-squad.html#availability')));
  assert.ok(intent.endsWith(';end'));
  assert.throws(() => androidIntent({ ...example, version:'x;package=bad' }), TypeError);
});
