/* Shared by the layered swatch books. Load after ../harness.js and link tokens.css.
   Each option is written once, as <section class="swatch" data-option="layer:option"> (or
   "start:<id>" for a starting point), drawn only with the shared colour names. On load this puts
   every swatch on a light page and a copy on a dark page, side by side, so both are always seen
   and both are measured by audit. A swatch with data-stack puts the two one above the other, full width. swatchTest() is the page's test: every option drawn, in both. */
function pairSwatches() {
  for (const sw of [...document.querySelectorAll('.swatch:not([data-mode])')]) {
    const pair = document.createElement('div');
    pair.className = 'pair';
    pair.dataset.pairOf = sw.dataset.option;
    if (sw.hasAttribute('data-stack')) pair.classList.add('stacked');
    sw.before(pair);
    const dark = sw.cloneNode(true);
    for (const el of [sw, ...sw.querySelectorAll('[id]')]) if (el.id) el.removeAttribute('id');
    for (const el of [dark, ...dark.querySelectorAll('[id]')]) if (el.id) el.removeAttribute('id');
    sw.classList.add('mode-light'); sw.dataset.mode = 'light';
    dark.classList.add('mode-dark'); dark.dataset.mode = 'dark';
    dark.setAttribute('aria-label', 'The same, on a dark page');
    pair.append(sw, dark);
  }
}
if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', pairSwatches); else pairSwatches();

async function swatchTest() {
  await sleep(300);
  const ids = [...new Set([...document.querySelectorAll('.swatch')].map((s) => s.dataset.option))];
  const wrong = [];
  for (const id of ids) {
    for (const mode of ['light', 'dark']) {
      const el = document.querySelector('.swatch[data-option="' + id + '"][data-mode="' + mode + '"]');
      const r = el && el.getBoundingClientRect();
      if (!r || r.width < 50 || r.height < 50) wrong.push(id + ' (' + mode + ')');
    }
  }
  const layers = ids.filter((id) => !id.startsWith('start:')).length;
  return { pass: layers >= 2 && !wrong.length,
           detail: ids.length + ' options shown, each on a light and a dark page: ' + ids.join(', ')
             + (wrong.length ? '; missing or drawn too small: ' + wrong.join(', ') : '') };
}
