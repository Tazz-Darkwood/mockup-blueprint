/* What a page is telling its visitor after some presses: alerts, live regions, open dialogs, anything classed as an
   error, and fields marked as wrong together with the text that describes them.
   Read and evaluated by blueprint.py; not copied into mockups. */
(() => {
  const seen = e => e.offsetHeight > 0 && !e.closest('#blueprint-viewer-root') && (!e.checkVisibility || e.checkVisibility());
  const words = e => e.innerText.trim().replace(/\s+/g, ' ').slice(0, 140);
  const found = new Set([...document.querySelectorAll('[role=alert], [role=status], [aria-live], dialog[open], [class*="error" i], [class*="invalid" i], [data-error]')].filter(seen));
  const invalid = [...document.querySelectorAll('[aria-invalid="true"], :user-invalid')].filter(seen);
  invalid.forEach(field => (field.getAttribute('aria-describedby') || '').split(/\s+/).forEach(id => { const d = id && document.getElementById(id); if (d && seen(d)) found.add(d); }));
  const messages = [...found].filter(e => ![...found].some(o => o !== e && o.contains(e))).map(words).filter(Boolean);
  return { messages: [...new Set(messages)], invalid: invalid.map(f => f.tagName.toLowerCase() + (f.id ? '#' + f.id : f.name ? '[name=' + f.name + ']' : '')) };
})()
