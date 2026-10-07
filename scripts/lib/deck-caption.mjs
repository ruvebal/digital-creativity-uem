/**
 * Minimal public caption HTML for the deck validator (PHASE-EX3).
 * Full deck renderer lands in EX5; this module only needs captionHtml for the
 * A12/F8 check (flagged asset must never read as "Public domain").
 */
import { caption } from './media-rules.mjs';

const PUBLIC_DOMAIN = 'Public domain';
const RIGHTS_UNDER_REVIEW = 'Rights under review';

const LICENCE_LABELS = Object.freeze({
  'PD-old-70': PUBLIC_DOMAIN,
  'PD-EU': PUBLIC_DOMAIN,
  PDM: PUBLIC_DOMAIN,
  CC0: 'CC0',
  'CC-BY-4.0': 'CC BY 4.0',
  'CC-BY-SA-4.0': 'CC BY-SA 4.0',
  'CC-BY-3.0': 'CC BY 3.0',
  'CC-BY-SA-3.0': 'CC BY-SA 3.0',
  'NoC-US+EU-checked': PUBLIC_DOMAIN,
});

function escapeHtml(value) {
  return String(value || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function isHttp(url) {
  return /^https?:\/\/\S+$/i.test(String(url || '').trim());
}

function link(href, label) {
  return `<a href="${escapeHtml(href)}" target="_blank" rel="noopener noreferrer">${escapeHtml(label)}</a>`;
}

function licenceLabel(licence) {
  return LICENCE_LABELS[String(licence || '').trim()] || String(licence || '').trim() || '';
}

/** One public caption line (title · author · licence · source). */
export function captionHtml(asset) {
  const c = caption(asset);
  const parts = [];
  if (c.title) parts.push(`<span class="slide-caption__title">${escapeHtml(c.title)}</span>`);
  if (c.author) parts.push(`<span class="slide-caption__author">${escapeHtml(c.author)}</span>`);
  const label = licenceLabel(c.licence);
  if (label && c.rights_status === 'flagged' && label === PUBLIC_DOMAIN) {
    parts.push(`<span class="slide-caption__rights">${escapeHtml(RIGHTS_UNDER_REVIEW)}</span>`);
  } else if (label) {
    parts.push(isHttp(c.licence_url) ? link(c.licence_url, label) : `<span>${escapeHtml(label)}</span>`);
  }
  if (isHttp(c.source_url)) parts.push(link(c.source_url, 'Source'));
  if (c.cropped) parts.push('<span>cropped</span>');
  return parts.join(' · ');
}
