/* What a phone-sized browser can measure. Thresholds come from library/style-mobile.md. Evaluated in the page; returns the measurements.
   Read and evaluated by blueprint.py; not copied into mockups. */
(() => {
  // the layout width, not innerWidth: a phone zooms out to fit a page that is too wide, and innerWidth grows with it
  const W = document.documentElement.clientWidth, H = document.documentElement.clientHeight;
  const rect = e => e.getBoundingClientRect();
  const mine = e => !!e.closest('#blueprint-viewer-root');
  const shown = e => { if (mine(e)) return false; if (e.checkVisibility && !e.checkVisibility()) return false;   // inside a closed <details>, for one
    const r = rect(e); if (r.width < 2 || r.height < 2) return false;
    const cs = getComputedStyle(e); return cs.visibility !== 'hidden' && cs.display !== 'none' && +cs.opacity !== 0; };
  const ownText = e => [...e.childNodes].filter(n => n.nodeType === 3).map(n => n.nodeValue).join(' ').replace(/\s+/g, ' ').trim();
  // getAttribute, not className: on a drawing (svg) className is not a string, and those were being named with no class at all
  const tagOf = e => { const c = (e.getAttribute('class') || '').trim();
    return '<' + e.tagName.toLowerCase() + (e.id ? '#' + e.id : '') + (c ? '.' + c.split(/\s+/)[0] : '') + '>'; };
  const say = e => { const t = (e.innerText || e.value || e.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 28);
    return tagOf(e) + (t ? ' "' + t + '"' : ''); };
  // a part of a drawing with no name of its own is named by the nearest thing round it that has one
  const sayWhere = e => { if (e.id || (e.getAttribute('class') || '').trim()) return say(e);
    const named = e.parentElement && e.parentElement.closest('[id], [class]');
    return say(e) + (named && named !== document.body ? ' inside ' + tagOf(named) : ''); };
  const all = [...document.querySelectorAll('body *')];

  // sideways scrolling, and what sticks out
  const sideways = document.documentElement.scrollWidth > W + 1;
  let culprits = [];
  if (sideways) {
    const over = all.filter(e => shown(e) && rect(e).right > W + 1 && rect(e).left < W);
    culprits = [...new Set(over.filter(e => !over.some(o => o !== e && e.contains(o))).map(sayWhere))].slice(0, 3);
  }

  // text sizes
  const small = [], running = [];
  all.forEach(e => { if (!shown(e)) return; const t = ownText(e); if (t.length < 2) return;
    const size = parseFloat(getComputedStyle(e).fontSize);
    if (size < 13.5) small.push([size, e]);
    else if (size < 15.5 && t.length >= 80 && e.closest('p, li, dd, blockquote, td')) running.push([size, e]); });

  // things you tap
  const sel = 'a[href], button, input:not([type=hidden]), select, textarea, summary, [role=button], [role=link], [role=tab], [onclick]';
  const taps = [...document.querySelectorAll(sel), ...all.filter(e => e.tagName.includes('-') && /button|checkbox|radio|switch|select|input|tab$/i.test(e.tagName) && !/group$/i.test(e.tagName))];
  const tiny = [], short = [];
  [...new Set(taps)].forEach(e => { if (!shown(e) || e.disabled) return;
    if (e.tagName === 'A' && getComputedStyle(e).display === 'inline' && ownText(e.parentElement).length > 0) return;  // a link inside a sentence
    let r = rect(e);
    if (e.tagName === 'INPUT' && /checkbox|radio/.test(e.type)) { const l = e.closest('label') || (e.id && document.querySelector('label[for="' + e.id + '"]')); if (l) r = rect(l); }
    if (r.width < 24 || r.height < 24) tiny.push(say(e) + ' ' + Math.round(r.width) + 'x' + Math.round(r.height));
    else if (r.height < 43.5) short.push(say(e) + ' ' + Math.round(r.height) + ' tall'); });

  // fields that make an iPhone zoom in
  const fields = [...document.querySelectorAll('input:not([type=hidden]):not([type=checkbox]):not([type=radio]):not([type=range]):not([type=button]):not([type=submit]), select, textarea')];
  all.forEach(e => { if (e.shadowRoot) fields.push(...e.shadowRoot.querySelectorAll('input:not([type=hidden]):not([type=checkbox]):not([type=radio]), select, textarea')); });
  const zoom = fields.filter(e => { const r = rect(e); return r.width > 1 && r.height > 1 && parseFloat(getComputedStyle(e).fontSize) < 15.5; }).length;

  // the first screen
  const h1 = [...document.querySelectorAll('h1')].find(shown);
  const h1r = h1 ? rect(h1) : null;
  const headingInFirst = h1 ? (h1r.top < H - 40 && h1r.bottom > 0) : null;

  // bars that stay on screen, measured one screen down
  scrollTo({ top: H, behavior: 'instant' });
  const bars = all.filter(e => { if (!shown(e)) return false; const p = getComputedStyle(e).position; if (p !== 'fixed' && p !== 'sticky') return false;
    const r = rect(e); return r.width > W * 0.6 && r.height < H * 0.6 && (r.top <= 1 || r.bottom >= H - 1) && r.bottom > 0 && r.top < H; });
  const outer = bars.filter(e => !bars.some(o => o !== e && o.contains(e)));
  const barShare = Math.round(100 * outer.reduce((a, e) => a + rect(e).height, 0) / H);

  // does a bar at the bottom cover the end of the page?
  scrollTo({ top: document.documentElement.scrollHeight, behavior: 'instant' });
  let covered = null;
  const bottomBars = outer.filter(e => shown(e) && rect(e).bottom >= H - 1 && rect(e).top > H / 2);
  if (bottomBars.length) {
    const barTop = Math.min(...bottomBars.map(e => rect(e).top));
    const last = all.filter(e => shown(e) && ownText(e).length > 1 && !bottomBars.some(b => b.contains(e)) && !bars.some(b => b.contains(e)))
      .sort((a, b) => rect(b).bottom - rect(a).bottom)[0];
    if (last && rect(last).bottom > barTop + 1 && rect(last).top < H) covered = say(last);
  }
  scrollTo({ top: 0, behavior: 'instant' });

  const sample = list => list.length ? { count: list.length, size: Math.round(Math.min(...list.map(x => x[0])) * 10) / 10, sample: ownText(list[0][1]).slice(0, 40) } : null;
  // a canvas that keeps every touch for itself, on a page that needs scrolling
  const canScroll = document.documentElement.scrollHeight > H + 200;
  const traps = canScroll ? [...document.querySelectorAll('canvas')].filter(c => shown(c) && rect(c).width > W * 0.5 && getComputedStyle(c).touchAction === 'none').length : 0;
  return { width: W, sideways, culprits, small: sample(small), running: sample(running), tiny, short, zoom, headingInFirst, barShare, covered, traps };
})()
