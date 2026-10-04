/* blueprint-viewer v2
   Shows the build context for this mockup (from the .blueprint.js file beside it):
   notes pinned to elements, open questions people can answer, and live checks.
   Review tooling only. It is not part of the design; do not port it to the real build. */
(function () {
  'use strict';
  if (window.__blueprint) return;

  var BP = window.__BLUEPRINT__ && typeof window.__BLUEPRINT__ === 'object' ? window.__BLUEPRINT__ : null;
  var FILE = decodeURIComponent(location.pathname.split('/').pop() || 'index.html');
  var STORE = 'blueprint:' + location.pathname;
  /* measure:begin (a copy of scripts/js/measure.js in the skill; do not edit here) */
/* blueprint measure 2
   The one copy of the code that measures a live page: which controls have no context, which custom
   tags never loaded, and where text is too faint to read. blueprint.py evaluates this file itself in
   every page it checks. blueprint-viewer.js carries an identical copy between its "measure" markers,
   for the Checks tab; `blueprint.py selftest` fails if the two differ. Change it here, then run
   `blueprint.py selftest --sync` to copy it into the viewer. */
var __bpMeasure = (function () {
  'use strict';
  var INTERACTIVE = 'a, button, form, input:not([type=hidden]), select, textarea, canvas, summary, [onclick], ' +
    '[role=button], [role=link], [role=tab], [role=menuitem], [role=switch], [role=checkbox]';

  // Rendered at all: has a box, is not hidden, and is not inside something closed (a <details>, say).
  // The phone measurements use a stricter test of their own, "a person could see it on the screen".
  function shown(el) {
    if (!el.getClientRects().length) return false;
    if (el.checkVisibility && !el.checkVisibility()) return false;
    return getComputedStyle(el).visibility !== 'hidden';
  }
  function labelOf(el) {
    var t = (el.getAttribute('aria-label') || el.textContent || el.getAttribute('placeholder') ||
      el.getAttribute('value') || el.getAttribute('name') || el.id || '').replace(/\s+/g, ' ').trim();
    return t.slice(0, 60) || '(no text)';
  }

  // custom elements (web components) that act as controls, recognised by the end of their tag name
  var CUSTOM = /-(button|copy-button|tab|menu-item|dropdown-item|option|input|textarea|select|combobox|checkbox|switch|radio-group|slider|range|rating|color-picker|file-input|number-input|toggle)$/;
  function interactiveEls() {
    var out = Array.prototype.slice.call(document.querySelectorAll(INTERACTIVE));
    document.querySelectorAll('*').forEach(function (el) {
      if (el.localName.indexOf('-') > 0 && CUSTOM.test(el.localName) && out.indexOf(el) < 0) out.push(el);
    });
    return out;
  }
  function uncovered() {
    return interactiveEls().filter(function (el) { return !el.closest('[data-bp]'); });
  }
  // custom elements the browser never upgraded: a misspelled tag, or the defining script is missing
  function neverLoaded() {
    var names = [];
    document.querySelectorAll(':not(:defined)').forEach(function (el) {
      if (names.indexOf(el.localName) < 0) names.push(el.localName);
    });
    return names;
  }

  function rgba(str) {
    var m = /^rgba?\(([^)]+)\)$/.exec(str);
    if (!m) return null;
    var p = m[1].split(/[\s,\/]+/).filter(Boolean).map(parseFloat);
    return p.length < 3 || p.some(isNaN) ? null : [p[0], p[1], p[2], p.length > 3 ? p[3] : 1];
  }
  function blend(top, under) {
    var a = top[3];
    return [top[0] * a + under[0] * (1 - a), top[1] * a + under[1] * (1 - a), top[2] * a + under[2] * (1 - a), 1];
  }
  function luminance(c) {
    var v = [c[0], c[1], c[2]].map(function (x) {
      x /= 255;
      return x <= 0.03928 ? x / 12.92 : Math.pow((x + 0.055) / 1.055, 2.4);
    });
    return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2];
  }
  function hex(c) {
    return '#' + [c[0], c[1], c[2]].map(function (x) {
      return ('0' + Math.round(x).toString(16)).slice(-2);
    }).join('');
  }
  // Colours painted behind an element's content by its own ::before and ::after: only ones that are
  // positioned, cover the whole element and sit beneath it (a negative z-index). Nearest the words first.
  // Null when one of them is a picture or gradient, so the colour cannot be known.
  function paintedBehind(el, words) {
    var found = [];
    // The same thing done with a real element: an empty child laid over the whole of `el`, with the words in a sibling
    // (utility-class frameworks make this the natural way to write it). If the words are visible at all, it is behind them.
    Array.prototype.forEach.call(el.children, function (child) {
      if (child === words || child.contains(words) || child.childElementCount || child.textContent.trim()) return;
      var ps = getComputedStyle(child);
      if (ps.display === 'none' || ps.visibility === 'hidden' || (ps.position !== 'absolute' && ps.position !== 'fixed') || parseFloat(ps.opacity) === 0) return;
      if ([ps.top, ps.right, ps.bottom, ps.left].some(function (side) { return !(parseFloat(side) <= 0.5); })) return;
      if (ps.backgroundImage !== 'none') { found.push({ z: -1, c: null }); return; }
      var c = rgba(ps.backgroundColor);
      if (!c || c[3] === 0) return;
      if (parseFloat(ps.opacity) < 1) c = [c[0], c[1], c[2], c[3] * parseFloat(ps.opacity)];
      found.push({ z: -1, c: c });
    });
    ['::before', '::after'].forEach(function (which) {
      var ps = getComputedStyle(el, which);
      if (!ps || ps.content === 'none' || ps.display === 'none' || ps.position !== 'absolute') return;
      var z = parseInt(ps.zIndex, 10), see = parseFloat(ps.opacity);
      if (!(z < 0) || see === 0) return;
      if ([ps.top, ps.right, ps.bottom, ps.left].some(function (side) { return !(parseFloat(side) <= 0.5); })) return;
      if (ps.backgroundImage !== 'none') { found.push({ z: z, c: null }); return; }
      var c = rgba(ps.backgroundColor);
      if (!c || c[3] === 0) return;
      if (see < 1) c = [c[0], c[1], c[2], c[3] * see];
      found.push({ z: z, c: c });
    });
    found.sort(function (a, b) { return b.z - a.z; });
    var out = [];
    for (var i = 0; i < found.length; i++) {
      if (!found[i].c) return null;
      out.push(found[i].c);
      if (found[i].c[3] === 1) break;
    }
    return out;
  }
  // Solid background behind an element, or null when it cannot be known (images, gradients, opacity).
  function backgroundOf(el) {
    var layers = [];
    for (var n = el; n && n.nodeType === 1; n = n.parentElement) {
      var cs = getComputedStyle(n);
      if (cs.backgroundImage !== 'none' || parseFloat(cs.opacity) < 1) return null;
      var c = rgba(cs.backgroundColor);
      if (!c) return null;
      // A shape drawn behind the words by ::before or ::after (cut paper, a tilted block) is their background.
      if (c[3] === 0 || cs.isolation === 'isolate' || cs.zIndex !== 'auto') {
        var behind = paintedBehind(n, el);
        if (behind === null) return null;
        if (behind.length) { layers = layers.concat(behind); if (behind[behind.length - 1][3] === 1) break; }
      }
      if (c[3] > 0) { layers.push(c); if (c[3] === 1) break; }
    }
    var out = layers.length && layers[layers.length - 1][3] === 1 ? layers.pop() : [255, 255, 255, 1];
    for (var i = layers.length - 1; i >= 0; i--) out = blend(layers[i], out);
    return out;
  }
  function contrastIssues() {
    var groups = {}, seen = [], count = 0;
    var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    var node;
    while ((node = walker.nextNode()) && count < 3000) {
      var text = node.nodeValue.replace(/\s+/g, ' ').trim();
      var p = node.parentElement;
      if (!text || !p || seen.indexOf(p) >= 0 || /^(SCRIPT|STYLE|NOSCRIPT|TEMPLATE)$/.test(p.tagName)) continue;
      seen.push(p); count++;
      if (!shown(p) || p.closest('[disabled], [aria-disabled="true"]')) continue;
      var cs = getComputedStyle(p);
      var fg = rgba(cs.color), bg = backgroundOf(p);
      if (!fg || !bg) continue;
      if (fg[3] < 1) fg = blend(fg, bg);
      var l1 = luminance(fg), l2 = luminance(bg);
      var ratio = (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
      var size = parseFloat(cs.fontSize), bold = parseInt(cs.fontWeight, 10) >= 700;
      var required = size >= 24 || (size >= 18.66 && bold) ? 3 : 4.5;
      if (ratio >= required) continue;
      var key = hex(fg) + ' on ' + hex(bg) + ' @' + required;
      var g = groups[key] || (groups[key] = {
        color: hex(fg), background: hex(bg), ratio: Math.floor(ratio * 100) / 100,
        required: required, count: 0, sample: text.slice(0, 40), el: p
      });
      g.count++;
    }
    return Object.keys(groups).map(function (k) { return groups[k]; })
      .sort(function (a, b) { return a.ratio - b.ratio; });
  }

  return {
    version: 2, shown: shown, labelOf: labelOf, interactiveEls: interactiveEls, uncovered: uncovered,
    neverLoaded: neverLoaded, contrastIssues: contrastIssues,
    report: function () {
      var described = (window.__BLUEPRINT__ && window.__BLUEPRINT__.elements) || {}, found = {};
      document.querySelectorAll('[data-bp]').forEach(function (el) { found[el.getAttribute('data-bp')] = true; });
      return {
        file: decodeURIComponent(location.pathname.split('/').pop() || 'index.html'),
        interactive: interactiveEls().length,
        neverLoaded: neverLoaded(),
        uncovered: uncovered().map(function (el) { return { tag: el.tagName.toLowerCase(), label: labelOf(el), visible: shown(el) }; }),
        contrast: contrastIssues().map(function (c) {
          return { color: c.color, background: c.background, ratio: c.ratio, required: c.required, count: c.count, sample: c.sample };
        }),
        anchorsOnPage: Object.keys(found),
        anchorsNotDescribed: Object.keys(found).filter(function (id) { return !described[id]; })
      };
    }
  };
})();
  /* measure:end */
  var shown = __bpMeasure.shown, labelOf = __bpMeasure.labelOf, uncovered = __bpMeasure.uncovered,
    neverLoaded = __bpMeasure.neverLoaded, contrastIssues = __bpMeasure.contrastIssues;
  var COLORS = { confirmed: '#15803d', inferred: '#b45309', open: '#b91c1c', mock: '#475569', unknown: '#6d28d9' };
  var LABELS = { confirmed: 'Confirmed', inferred: 'Inferred', open: 'Open' };
  var SECTIONS = ['summary', 'audience', 'scope', 'fidelity', 'data_model', 'auth', 'integrations', 'stack',
    'deployment', 'accessibility', 'security', 'requirements', 'content'];

  var project = (BP && BP.project) || {};
  var elements = (BP && BP.elements) || {};
  var screens = (BP && BP.screens) || [];
  var questions = (BP && BP.questions) || [];
  var ids = Object.keys(elements);

  var state = { open: false, mini: false, tab: 'overview', side: 'right', selected: null, flash: null, flashUntil: 0 };
  var feedback = { answers: {}, comments: {} };
  try {
    var saved = JSON.parse(localStorage.getItem(STORE) || '{}');
    feedback.answers = saved.answers || {};
    feedback.comments = saved.comments || {};
    state.open = !!saved.open;
    state.side = saved.side === 'left' ? 'left' : 'right';
    state.mini = !!saved.mini;
  } catch (e) { /* storage unavailable: the viewer still works, it just forgets */ }
  if (/blueprint/.test(location.hash)) state.open = true;

  function persist() {
    try {
      localStorage.setItem(STORE, JSON.stringify({
        answers: feedback.answers, comments: feedback.comments, open: state.open, side: state.side, mini: state.mini
      }));
    } catch (e) { /* ignore */ }
  }

  // ---------------------------------------------------------------- helpers

  function h(tag, props) {
    var n = document.createElement(tag);
    props = props || {};
    Object.keys(props).forEach(function (k) {
      if (k === 'class') n.className = props[k];
      else if (k === 'text') n.textContent = props[k];
      else if (k.slice(0, 2) === 'on') n.addEventListener(k.slice(2), props[k]);
      else n.setAttribute(k, props[k]);
    });
    for (var i = 2; i < arguments.length; i++) add(n, arguments[i]);
    return n;
  }
  function add(parent, child) {
    if (child == null || child === false) return;
    if (Array.isArray(child)) child.forEach(function (c) { add(parent, c); });
    else parent.appendChild(typeof child === 'string' ? document.createTextNode(child) : child);
  }
  function humanize(key) {
    var s = String(key).replace(/_/g, ' ');
    return s.charAt(0).toUpperCase() + s.slice(1);
  }
  function empty(v) {
    return v == null || v === '' || (Array.isArray(v) && !v.length) ||
      (typeof v === 'object' && !Array.isArray(v) && !Object.keys(v).length);
  }
  function value(v) {
    if (empty(v)) return h('p', { class: 'muted', text: 'Not stated' });
    if (typeof v !== 'object') return h('p', { text: String(v) });
    if (Array.isArray(v)) {
      return h('ul', {}, v.map(function (x) {
        return x && typeof x === 'object' ? h('li', {}, value(x)) : h('li', { text: String(x) });
      }));
    }
    var dl = h('dl');
    Object.keys(v).forEach(function (k) {
      if (empty(v[k])) return;
      add(dl, [h('dt', { text: humanize(k) }), h('dd', {}, value(v[k]))]);
    });
    return dl;
  }
  function chip(status, text) {
    var c = h('span', { class: 'chip', text: text || LABELS[status] || 'No status' });
    c.style.background = COLORS[status] || COLORS.unknown;
    return c;
  }
  function statusOf(id) {
    var e = elements[id];
    if (!e) return 'unknown';
    return e.mock_only ? 'mock' : (LABELS[e.status] ? e.status : 'unknown');
  }
  function findAnchor(id) {
    var all = document.querySelectorAll('[data-bp]');
    var first = null;
    for (var i = 0; i < all.length; i++) {
      if (all[i].getAttribute('data-bp') !== id) continue;
      if (shown(all[i])) return all[i];
      first = first || all[i];
    }
    return first;
  }
  function screenOf(id) {
    if (elements[id] && elements[id].screen) return elements[id].screen;
    var el = findAnchor(id);
    var s = el && el.closest('[data-bp-screen]');
    return s ? s.getAttribute('data-bp-screen') : null;
  }
  function screenInfo(sid) {
    for (var i = 0; i < screens.length; i++) if (screens[i].id === sid) return screens[i];
    return null;
  }
  // What an unanswered question holds up: 'build', 'launch' or nothing. `blocking: true` is the older spelling of build.
  function blocks(q) { return q.blocks || (q.blocking ? 'build' : null); }
  function openQuestions() {
    return questions.filter(function (q) { return empty(q.answer) && empty(q.closed); });   // closed: withdrawn or settled elsewhere
  }

  // ---------------------------------------------------------------- shell

  var host = document.createElement('div');
  host.id = 'blueprint-viewer-root';
  var root = host.attachShadow({ mode: 'open' });
  var css = document.createElement('style');
  css.textContent = [
    ':host{all:initial}',
    '*{box-sizing:border-box}',
    '.layer{position:fixed;inset:0;pointer-events:none;z-index:2147483000}',
    '.mark{position:absolute;border:2px solid var(--c);border-radius:4px}',
    '.mark.sel{box-shadow:0 0 0 4px rgba(37,99,235,.4);border-style:solid}',
    '.mark.flash{border:3px dashed #b91c1c;box-shadow:0 0 0 4px rgba(185,28,28,.25)}',
    '.badge{position:absolute;top:-14px;left:-14px;min-width:20px;height:20px;padding:0 5px;border:0;border-radius:10px;' +
      'background:var(--c);color:#fff;font:600 11px/20px system-ui,sans-serif;text-align:center;pointer-events:auto;cursor:pointer}',
    '.fab{position:fixed;right:16px;bottom:16px;z-index:2147483001;border:0;border-radius:999px;padding:10px 16px;' +
      'background:#111827;color:#fff;font:600 13px/1 system-ui,sans-serif;cursor:pointer;box-shadow:0 4px 14px rgba(0,0,0,.3)}',
    '.fab b{background:#b91c1c;border-radius:999px;padding:2px 7px;margin-left:8px;font-weight:600}',
    '.mini{position:fixed;right:16px;bottom:16px;z-index:2147483001;display:flex;gap:2px;padding:4px;border-radius:999px;' +
      'background:#111827;box-shadow:0 4px 14px rgba(0,0,0,.3)}',
    '.mini.left{right:auto;left:16px}',
    '.mini button{border:0;border-radius:999px;padding:8px 12px;background:transparent;color:#fff;' +
      'font:600 13px/1 system-ui,sans-serif;cursor:pointer}',
    '.mini button:hover{background:#374151}',
    '.panel{position:fixed;top:0;right:0;z-index:2147483001;width:min(420px,94vw);height:100vh;display:flex;' +
      'flex-direction:column;background:#fff;color:#111827;font:14px/1.5 system-ui,sans-serif;' +
      'border-left:1px solid #d1d5db;box-shadow:0 0 24px rgba(0,0,0,.18)}',
    '.panel.left{right:auto;left:0;border-left:0;border-right:1px solid #d1d5db}',
    '.head{display:flex;align-items:center;gap:8px;padding:12px 14px;border-bottom:1px solid #e5e7eb}',
    '.head h1{flex:1;margin:0;font-size:15px;font-weight:700;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}',
    '.icon{border:1px solid #d1d5db;background:#fff;color:#111827;border-radius:6px;min-width:30px;height:30px;' +
      'font:14px/1 system-ui,sans-serif;cursor:pointer}',
    '.tabs{display:flex;border-bottom:1px solid #e5e7eb}',
    '.tabs button{flex:1 1 auto;padding:10px 4px;border:0;border-bottom:3px solid transparent;background:none;color:#4b5563;' +
      'font:600 12.5px/1 system-ui,sans-serif;white-space:nowrap;cursor:pointer}',
    '.tabs button[aria-selected=true]{color:#111827;border-bottom-color:#111827}',
    'button:focus-visible,textarea:focus-visible,a:focus-visible{outline:2px solid #2563eb;outline-offset:2px}',
    '.body{flex:1;overflow:auto;padding:14px}',
    '.foot{padding:10px 14px;border-top:1px solid #e5e7eb;background:#f9fafb}',
    '.foot button{width:100%;padding:9px;border:0;border-radius:6px;background:#111827;color:#fff;' +
      'font:600 13px/1 system-ui,sans-serif;cursor:pointer}',
    '.foot button[disabled]{background:#d1d5db;color:#4b5563;cursor:default}',
    '.foot p{margin:8px 0 0;font-size:12px;color:#4b5563}',
    'h2{margin:18px 0 6px;font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:.04em;color:#374151;' +
      'display:flex;align-items:center;gap:8px}',
    'h2:first-child{margin-top:0}',
    'h3{margin:0;font-size:14px;font-weight:700;flex:1}',
    'p{margin:0 0 6px;white-space:pre-wrap;overflow-wrap:anywhere}',
    'ul{margin:0 0 6px;padding-left:18px}',
    'dl{margin:0}',
    'dt{font-size:12px;font-weight:700;color:#4b5563;margin-top:6px}',
    'dd{margin:0}',
    '.muted{color:#4b5563}',
    '.chip{display:inline-block;border-radius:999px;padding:1px 8px;color:#fff;font-size:11px;font-weight:600;white-space:nowrap}',
    '.card{border:1px solid #e5e7eb;border-left:4px solid var(--c,#d1d5db);border-radius:6px;padding:10px 12px;margin:0 0 10px}',
    '.card.sel{background:#eff6ff;border-color:#2563eb;border-left-color:#2563eb}',
    '.card .top{display:flex;align-items:center;gap:8px;margin-bottom:4px}',
    '.card .num{min-width:22px;height:22px;border-radius:11px;background:var(--c);color:#fff;font-size:11px;font-weight:600;' +
      'line-height:22px;text-align:center;padding:0 6px}',
    '.link{border:0;background:none;padding:0;color:#1d4ed8;font:inherit;text-decoration:underline;cursor:pointer;text-align:left}',
    '.q{background:#fef2f2;border-radius:4px;padding:6px 8px;margin-top:6px;font-size:13px}',
    'textarea{display:block;width:100%;min-height:56px;margin-top:8px;padding:6px 8px;border:1px solid #9ca3af;border-radius:4px;' +
      'background:#fff;color:#111827;font:13px/1.4 system-ui,sans-serif;resize:vertical}',
    '.swatch{display:inline-block;width:12px;height:12px;border:1px solid #9ca3af;border-radius:2px;vertical-align:-1px;margin-right:4px}',
    '.error{background:#fef2f2;border:1px solid #fecaca;border-radius:6px;padding:10px 12px}',
    '@media print{:host{display:none}}'
  ].join('\n');
  root.appendChild(css);

  var layer = h('div', { class: 'layer', 'aria-hidden': 'true' });
  var fab = h('button', { class: 'fab', type: 'button', onclick: function () { setOpen(true); } });
  // shrunk state: the panel is out of the way but the pins stay on the page
  var mini = h('div', { class: 'mini' },
    h('button', { type: 'button', text: 'Open notes', onclick: function () { state.mini = false; persist(); render(); } }),
    h('button', { type: 'button', 'aria-label': 'Hide blueprint pins', text: '✕', onclick: function () { setOpen(false); } }));
  var body = h('div', { class: 'body' });
  var tabs = h('div', { class: 'tabs', role: 'tablist' });
  var foot = h('div', { class: 'foot' });
  var panel = h('aside', { class: 'panel', 'aria-label': 'Blueprint context' },
    h('div', { class: 'head' },
      h('h1', { text: (project.name || FILE) + ' blueprint' }),
      h('button', { class: 'icon', type: 'button', 'aria-label': 'Move panel to the other side', text: '⇄',
        onclick: function () { state.side = state.side === 'left' ? 'right' : 'left'; persist(); render(); } }),
      h('button', { class: 'icon', type: 'button', 'aria-label': 'Shrink panel and keep the pins', text: '−',
        onclick: function () { state.mini = true; persist(); render(); } }),
      h('button', { class: 'icon', type: 'button', 'aria-label': 'Close blueprint panel', text: '✕',
        onclick: function () { setOpen(false); } })),
    tabs, body, foot);
  add(root, [layer, fab, mini, panel]);

  // ---------------------------------------------------------------- markers on the page

  var pool = [];
  function marker(i) {
    if (pool[i]) return pool[i];
    var badge = h('button', { class: 'badge', type: 'button' });
    var box = h('div', { class: 'mark' }, badge);
    badge.addEventListener('click', function () { select(box.__id, false); });
    layer.appendChild(box);
    return (pool[i] = box);
  }
  function place(box, r) {
    box.style.display = '';
    box.style.left = (r.left - 3) + 'px';
    box.style.top = (r.top - 3) + 'px';
    box.style.width = (r.width + 6) + 'px';
    box.style.height = (r.height + 6) + 'px';
    // the badge sits just outside the top-left corner, pulled in when that would leave the viewport
    box.firstChild.style.left = Math.max(-14, 5 - r.left) + 'px';
    box.firstChild.style.top = Math.max(-14, 5 - r.top) + 'px';
  }
  function sync() {
    var n = 0;
    if (state.open) {
      var all = document.querySelectorAll('[data-bp]');
      for (var i = 0; i < all.length; i++) {
        var r = all[i].getBoundingClientRect();
        if (!r.width || !r.height || r.bottom < 0 || r.top > innerHeight || r.right < 0 || r.left > innerWidth) continue;
        if (getComputedStyle(all[i]).visibility === 'hidden') continue;
        var id = all[i].getAttribute('data-bp');
        var box = marker(n++);
        box.__id = id;
        box.className = 'mark' + (id === state.selected ? ' sel' : '');
        box.style.setProperty('--c', COLORS[statusOf(id)]);
        var num = ids.indexOf(id);
        box.firstChild.textContent = num >= 0 ? String(num + 1) : '?';
        box.firstChild.setAttribute('aria-label', 'Show context for ' + ((elements[id] && elements[id].name) || id));
        place(box, r);
      }
      if (state.flash && Date.now() < state.flashUntil && document.contains(state.flash)) {
        var f = marker(n++);
        f.className = 'mark flash';
        f.firstChild.style.display = 'none';
        place(f, state.flash.getBoundingClientRect());
      }
    }
    for (var j = n; j < pool.length; j++) pool[j].style.display = 'none';
    for (var k = 0; k < n; k++) if (pool[k].className.indexOf('flash') < 0) pool[k].firstChild.style.display = '';
  }
  // Keep the Blueprint button and the shrunk bar clear of anything the mockup itself pins to the
  // bottom of the screen (a phone call bar, a cookie banner), so they never cover its controls.
  function dock() {
    var x = state.side === 'left' ? 60 : innerWidth - 60, bottom = 16;
    var stack = document.elementsFromPoint ? document.elementsFromPoint(x, innerHeight - 30) : [];
    stack.forEach(function (el) {
      for (var n = el; n && n.nodeType === 1 && n !== host && n !== document.body; n = n.parentElement) {
        if (getComputedStyle(n).position !== 'fixed') continue;
        var r = n.getBoundingClientRect();
        if (r.height < innerHeight / 2) bottom = Math.max(bottom, Math.round(innerHeight - r.top) + 12);
      }
    });
    fab.style.bottom = mini.style.bottom = bottom + 'px';
  }
  var queued = false;
  function queueSync() {
    if (queued) return;
    queued = true;
    requestAnimationFrame(function () { queued = false; sync(); });
  }
  window.addEventListener('scroll', queueSync, true);
  window.addEventListener('resize', function () { dock(); queueSync(); });
  setInterval(function () { sync(); dock(); }, 500);   // catches tab switches, modals, bars that appear later and other DOM changes in the mockup

  function flash(el) {
    el.scrollIntoView({ block: 'center', behavior: 'smooth' });
    state.flash = el;
    state.flashUntil = Date.now() + 2500;
    queueSync();
  }
  function select(id, scrollPage) {
    if (state.mini) { state.mini = false; persist(); }
    state.selected = id;
    state.tab = 'elements';
    render();
    var card = root.getElementById('card-' + id);
    if (card) card.scrollIntoView({ block: 'nearest' });
    var el = findAnchor(id);
    if (scrollPage && el && shown(el)) el.scrollIntoView({ block: 'center', behavior: 'smooth' });
    queueSync();
  }

  // ---------------------------------------------------------------- panel tabs

  function overview() {
    var out = [];
    var status = project.status || {};
    if (project.ref) out.push(h('p', { text: 'Project context lives in ' + project.ref }));
    SECTIONS.concat(Object.keys(project).filter(function (k) {
      return SECTIONS.indexOf(k) < 0 && k !== 'name' && k !== 'status';
    })).forEach(function (k) {
      if (!(k in project)) return;
      out.push(h('h2', {}, humanize(k), status[k] ? chip(status[k]) : null));
      out.push(value(project[k]));
    });
    if (screens.length) {
      out.push(h('h2', { text: 'Screens' }));
      screens.forEach(function (s) {
        var c = h('div', { class: 'card' },
          h('div', { class: 'top' }, h('h3', { text: s.name || s.id }), s.status ? chip(s.status) : null));
        c.style.setProperty('--c', COLORS[s.status] || '#d1d5db');
        var rest = {};
        Object.keys(s).forEach(function (k) { if (['id', 'name', 'status'].indexOf(k) < 0) rest[k] = s[k]; });
        add(c, value(rest));
        if (s.file && s.file !== FILE) {
          if (ownPage(s.file)) add(c, h('a', { href: s.file + '#blueprint', text: 'Open ' + s.file }));
          else add(c, h('span', { text: String(s.file) }));
        }
        out.push(c);
      });
    }
    (BP.flows || []).forEach(function (f, i) {
      if (!i) out.push(h('h2', { text: 'Flows' }));
      out.push(h('h3', { text: f.name || 'Flow' }));
      out.push(h('ol', {}, (f.steps || []).map(function (s) { return h('li', { text: String(s) }); })));
    });
    return out;
  }

  function questionBlock(q) {
    var b = blocks(q);
    return h('div', { class: 'q' }, h('strong', { text: b === 'build' ? 'Blocks the build: ' : b === 'launch' ? 'Needed before launch: ' : 'Question: ' }), String(q.question || ''));
  }
  function noteBox(kind, key, placeholder, label) {
    var t = h('textarea', { placeholder: placeholder, 'aria-label': label });
    t.value = feedback[kind][key] || '';
    t.addEventListener('input', function () {
      if (t.value.trim()) feedback[kind][key] = t.value; else delete feedback[kind][key];
      persist();
      renderFoot();
    });
    return t;
  }

  function elementCard(id) {
    var e = elements[id] || {};
    var st = statusOf(id);
    var el = findAnchor(id);
    var card = h('div', { class: 'card' + (id === state.selected ? ' sel' : ''), id: 'card-' + id },
      h('div', { class: 'top' },
        h('span', { class: 'num', text: String(ids.indexOf(id) + 1) }),
        h('h3', {}, h('button', { class: 'link', type: 'button', text: e.name || id,
          onclick: function () { select(id, true); } })),
        st === 'mock' ? chip('mock', 'Mockup only') : chip(st)));
    card.style.setProperty('--c', COLORS[st]);
    if (!el) add(card, h('p', { class: 'muted', text: e.not_in_mockup
      ? 'Not drawn in the mockup. To be built from this description.' : 'Not on this page.' }));
    else if (!shown(el)) add(card, h('p', { class: 'muted', text: 'Hidden in the current state of the page.' }));
    var rest = {};
    ['does', 'data', 'states', 'rules', 'access', 'a11y', 'acceptance', 'notes'].concat(Object.keys(e)).forEach(function (k) {
      if (['name', 'status', 'screen', 'mock_only', 'not_in_mockup'].indexOf(k) < 0 && !empty(e[k])) rest[k] = e[k];
    });
    add(card, value(rest));
    openQuestions().forEach(function (q) { if (q.about === id) add(card, questionBlock(q)); });
    add(card, noteBox('comments', id, 'Something wrong or missing here? Add a note.', 'Note about ' + (e.name || id)));
    return card;
  }

  function elementsTab() {
    var here = {}, elsewhere = [], out = [];
    ids.forEach(function (id) {
      var sid = screenOf(id);
      var info = sid && screenInfo(sid);
      // On a mockup of several pages, most elements live on another page: list those briefly, do not show their cards.
      if (!findAnchor(id) && !(elements[id] && elements[id].not_in_mockup)) {
        elsewhere.push([id, info && info.file && info.file !== FILE ? info.file : null]); return;
      }
      (here[sid || ''] = here[sid || ''] || []).push(id);
    });
    Object.keys(here).forEach(function (sid) {
      var info = screenInfo(sid);
      out.push(h('h2', { text: sid ? ((info && info.name) || sid) : 'Shared / no screen' }));
      here[sid].forEach(function (id) { out.push(elementCard(id)); });
    });
    var strays = [];
    document.querySelectorAll('[data-bp]').forEach(function (el) {
      var id = el.getAttribute('data-bp');
      if (!elements[id] && strays.indexOf(id) < 0) strays.push(id);
    });
    if (strays.length) {
      out.push(h('h2', { text: 'Marked on the page but not described' }));
      out.push(h('ul', {}, strays.map(function (id) { return h('li', { text: id }); })));
    }
    if (elsewhere.length) {
      out.push(h('h2', { text: 'Not on this page' }));
      out.push(h('ul', {}, elsewhere.map(function (x) {
        var name = elements[x[0]].name || x[0];
        return x[1] && ownPage(x[1]) ? h('li', {}, name + ', on ', h('a', { href: x[1] + '#blueprint', text: x[1] })) : h('li', { text: name });
      })));
    }
    if (!out.length) out.push(h('p', { class: 'muted', text: 'No elements have context yet.' }));
    return out;
  }

  function questionsTab() {
    if (!questions.length) return [h('p', { class: 'muted', text: 'No questions recorded.' })];
    var sorted = questions.slice().sort(function (a, b) {
      // open before answered; among the open, anything marked urgent first, then what holds up the build, then the launch
      var rank = function (q) { return (empty(q.answer) && empty(q.closed) ? 0 : 4) + (q.urgent ? 0 : blocks(q) === 'build' ? 1 : blocks(q) === 'launch' ? 2 : 3); };
      return rank(a) - rank(b);
    });
    return sorted.map(function (q) {
      var done = !empty(q.answer);
      var card = h('div', { class: 'card' },
        h('div', { class: 'top' },
          h('h3', { text: String(q.question || '') }),
          done ? chip('confirmed', 'Answered') : blocks(q) === 'build' ? chip('open', 'Blocks the build')
            : blocks(q) === 'launch' ? chip('inferred', 'Needed before launch') : chip('mock', 'Open')));
      card.style.setProperty('--c', done ? COLORS.confirmed : blocks(q) === 'build' ? COLORS.open
        : blocks(q) === 'launch' ? COLORS.inferred : COLORS.mock);
      var about = elements[q.about]
        ? h('button', { class: 'link', type: 'button', text: elements[q.about].name || q.about,
          onclick: function () { select(q.about, true); } })
        : String(q.about || '');
      add(card, h('p', { class: 'muted' }, 'About: ', about));
      if (q.suggested) add(card, h('p', {}, h('strong', { text: 'If nobody says otherwise: ' }), String(q.suggested)));
      if (q.note) add(card, h('p', {}, h('strong', { text: 'Note: ' }), String(q.note)));
      if (q.ask) add(card, h('p', { class: 'muted', text: 'Best person to ask: ' + q.ask }));
      if (done) add(card, h('p', {}, h('strong', { text: 'Answer: ' }), String(q.answer)));
      else add(card, noteBox('answers', q.id, 'Type your answer', 'Answer to: ' + q.question));
      return card;
    });
  }

  function checksTab() {
    var out = [h('p', { class: 'muted', text: 'Checked against the page as it is shown right now. Switch screens or open dialogs in the mockup, then refresh.' }),
      h('p', {}, h('button', { class: 'link', type: 'button', text: 'Refresh checks', onclick: render }))];
    var gaps = uncovered();
    out.push(h('h2', {}, 'No context yet', chip(gaps.length ? 'open' : 'confirmed', String(gaps.length))));
    if (!gaps.length) out.push(h('p', { text: 'Every button, link, form and input is covered by a note.' }));
    else out.push(h('ul', {}, gaps.map(function (el) {
      return h('li', {}, h('button', { class: 'link', type: 'button',
        text: '<' + el.tagName.toLowerCase() + '> ' + labelOf(el) + (shown(el) ? '' : ' (hidden)'),
        onclick: function () { if (shown(el)) flash(el); } }));
    })));
    var dead = neverLoaded();
    if (dead.length) {
      out.push(h('h2', {}, 'Components that never loaded', chip('open', String(dead.length))));
      out.push(h('p', { text: 'A misspelled tag, or the script that defines it is missing:' }));
      out.push(h('ul', {}, dead.map(function (name) { return h('li', { text: '<' + name + '>' }); })));
    }
    var contrast = contrastIssues();
    out.push(h('h2', {}, 'Low contrast text', chip(contrast.length ? 'inferred' : 'confirmed', String(contrast.length))));
    if (!contrast.length) out.push(h('p', { text: 'No text below the WCAG AA contrast ratio on solid backgrounds.' }));
    else out.push(h('ul', {}, contrast.map(function (c) {
      var fg = h('span', { class: 'swatch' }), bg = h('span', { class: 'swatch' });
      fg.style.background = c.color; bg.style.background = c.background;
      return h('li', {}, fg, c.color + ' on ', bg, c.background + ': ' + c.ratio + ':1, needs ' + c.required + ':1. ',
        h('button', { class: 'link', type: 'button', text: c.count + ' place(s), e.g. "' + c.sample + '"',
          onclick: function () { flash(c.el); } }));
    })));
    out.push(h('p', { class: 'muted', text: 'Text over images or gradients is not measured.' }));
    return out;
  }

  // ---------------------------------------------------------------- feedback export

  // A page of this mockup: a plain relative .html name. Anything else in a context file (another site, a script address) is shown as text, not as a link.
  function ownPage(name) { return typeof name === 'string' && /^[^:\\\/?#][^:?#]*\.html?$/i.test(name) && name.indexOf('..') < 0; }
  // What someone typed, laid out so that a line of theirs can never be read as the start of another answer or note.
  function typed(text) { return String(text).replace(/\r?\n/g, '\n   | '); }
  function feedbackText() {
    var lines = ['BLUEPRINT FEEDBACK', 'File: ' + FILE, 'Date: ' + new Date().toISOString().slice(0, 10), ''];
    pendingAnswers().forEach(function (q) {
      lines.push('ANSWER ' + q.id + ' (about: ' + q.about + ')', 'Q: ' + q.question, 'A: ' + typed(feedback.answers[q.id]), '');
    });
    Object.keys(feedback.comments).forEach(function (id) {
      lines.push('NOTE on ' + id + ' (' + ((elements[id] && elements[id].name) || 'unknown') + ')', '   | ' + typed(feedback.comments[id]), '');
    });
    return lines.join('\n');
  }
  // Answers typed here for questions the context has since recorded an answer to are already merged: leave them out.
  function pendingAnswers() {
    // not again: what was already merged, what was heard and left open (q.heard), and questions since closed
    return questions.filter(function (q) { return feedback.answers[q.id] && empty(q.answer) && empty(q.closed) && String(feedback.answers[q.id]).trim() !== String(q.heard || '').trim(); });
  }
  function feedbackCount() {
    return pendingAnswers().length + Object.keys(feedback.comments).length;
  }
  function copyFeedback() {
    var text = feedbackText();
    var done = function () {
      renderFoot('Copied. Paste it to whoever looks after this blueprint (or straight to Claude).');
    };
    var fallback = function () {
      var t = h('textarea', { 'aria-label': 'Your answers and notes', readonly: '' });
      t.value = text;
      foot.appendChild(t);
      t.select();
      renderFootNote('Copy the text above and send it to whoever looks after this blueprint.');
    };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(done, fallback);
    else fallback();
  }
  function renderFootNote(text) {
    foot.appendChild(h('p', { text: text }));
  }
  function renderFoot(message) {
    foot.textContent = '';
    var n = feedbackCount();
    var b = h('button', { type: 'button', text: n ? 'Copy my ' + n + ' answer(s) and note(s)' : 'No answers or notes yet',
      onclick: copyFeedback });
    if (!n) b.setAttribute('disabled', '');
    foot.appendChild(b);
    if (message) renderFootNote(message);
  }

  // ---------------------------------------------------------------- render

  var TABS = [['overview', 'Overview'], ['elements', 'Elements'], ['questions', 'Questions'], ['checks', 'Checks']];
  function render() {
    var pending = openQuestions().length;
    fab.textContent = 'Blueprint';
    // on a phone-sized screen the button is smaller and a little see-through, so it hides less of the mockup
    var narrow = function () { var small = window.innerWidth < 480; fab.style.transform = small ? 'scale(0.78)' : ''; fab.style.transformOrigin = 'bottom right'; fab.style.opacity = small ? '0.88' : ''; };
    narrow(); window.addEventListener('resize', narrow);
    if (pending) fab.appendChild(h('b', { text: pending + (pending === 1 ? ' question' : ' questions') }));
    var full = state.open && !state.mini;
    fab.style.display = state.open ? 'none' : '';
    panel.style.display = full ? '' : 'none';
    panel.className = 'panel' + (state.side === 'left' ? ' left' : '');
    mini.style.display = state.open && state.mini ? '' : 'none';
    mini.className = 'mini' + (state.side === 'left' ? ' left' : '');
    dock();
    if (!full) { sync(); return; }
    tabs.textContent = '';
    TABS.forEach(function (t) {
      var label = t[1] + (t[0] === 'questions' && pending ? ' (' + pending + ')' : '');
      tabs.appendChild(h('button', { type: 'button', role: 'tab', 'aria-selected': String(state.tab === t[0]), text: label,
        onclick: function () { state.tab = t[0]; render(); } }));
    });
    body.textContent = '';
    if (!BP) {
      add(body, h('div', { class: 'error' },
        h('p', {}, h('strong', { text: 'The context file did not load.' })),
        h('p', { text: 'The .blueprint.js file next to this mockup is missing, was not sent along with it, or has a syntax error. The Checks tab still works.' })));
      if (state.tab !== 'checks') { add(body, checksTab()); renderFoot(); sync(); return; }
    }
    add(body, state.tab === 'elements' ? elementsTab() : state.tab === 'questions' ? questionsTab()
      : state.tab === 'checks' ? checksTab() : overview());
    renderFoot();
    sync();
  }
  function setOpen(open) {
    state.open = open;
    if (open) state.mini = false;
    persist();
    render();
  }

  // What only a browser can see, for tools that drive the page headlessly.
  window.__blueprint = {
    version: 2,
    open: function () { setOpen(true); },
    close: function () { setOpen(false); },
    report: function () { return __bpMeasure.report(); }
  };

  function start() {
    document.documentElement.appendChild(host);
    render();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
