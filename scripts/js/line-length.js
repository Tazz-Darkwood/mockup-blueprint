/* The longest line of reading text, in characters, at the width the page is open at. Evaluated in the page by
   blueprint.py; not copied into mockups. Reading text: paragraphs and list items of three lines or more. A line is
   counted from where the browser actually broke it, so it is the real figure, not one worked out from a width. */
(() => {
  let worst = null;
  document.querySelectorAll('p, li, dd, blockquote').forEach(el => {
    if (el.closest('#blueprint-viewer-root, nav, header, footer, [aria-hidden="true"]')) return;
    if (el.querySelector('p, li, dd, blockquote')) return;   // the innermost block only
    const text = el.textContent.replace(/\s+/g, ' ').trim();
    if (text.length < 120 || (el.checkVisibility && !el.checkVisibility())) return;
    const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT), lines = new Map(), range = document.createRange();
    let node;
    while ((node = walker.nextNode())) {
      for (let i = 0; i < node.data.length; i++) {
        if (/\s/.test(node.data[i])) continue;
        range.setStart(node, i); range.setEnd(node, i + 1);
        const r = range.getBoundingClientRect();
        if (!r.height) continue;
        const key = Math.round(r.top + r.height / 2);
        let line = null;
        for (const [k, v] of lines) if (Math.abs(k - key) <= r.height * 0.4) { line = v; break; }
        if (!line) { line = { n: 0 }; lines.set(key, line); }
        line.n += 1;
      }
    }
    if (lines.size < 3) return;
    const counts = [...lines.values()].map(l => l.n).sort((a, b) => b - a);
    const spaces = Math.round(text.split(' ').length / lines.size);   // spaces were skipped above: add each line's share back
    const longest = counts[1] + spaces;   // the second longest: a single over-long line is often a long word wrapped late
    if (!worst || longest > worst.chars) worst = { chars: longest, sample: text.slice(0, 40), lines: lines.size };
  });
  return worst;
})()
