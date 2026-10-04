/* Lists the canvases on a page with what they draw and what stands in for them.
   Read and evaluated by blueprint.py; not copied into mockups. */
(() => {
  const path = (e) => { const parts = []; while (e && e !== document.body && e.parentElement) { parts.unshift(e.tagName.toLowerCase() + ':nth-child(' + ([...e.parentElement.children].indexOf(e) + 1) + ')'); e = e.parentElement; } return 'body > ' + parts.join(' > '); };
  return [...document.querySelectorAll('canvas')].filter((c) => !c.closest('#blueprint-viewer-root') && c.getBoundingClientRect().width > 1).map((c, i) => {
    const anchor = c.closest('[data-bp]');
    c.setAttribute('data-bp-canvas', i);
    return { index: i, is3d: /webgl/.test(c.__bpKind || ''), anchor: anchor ? anchor.getAttribute('data-bp') : null, holder: c.parentElement ? path(c.parentElement) : null,
             named: !!(c.getAttribute('aria-label') || c.getAttribute('aria-labelledby') || c.getAttribute('title') || c.textContent.trim()) };
  });
})()
