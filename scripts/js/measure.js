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
      if (see === 0 || [ps.top, ps.right, ps.bottom, ps.left].some(function (side) { return !(parseFloat(side) <= 0.5); })) return;
      // A texture laid over the whole box (grain, stains, a darkened edge) changes what the words sit on whether it is
      // drawn below them or blended over them: the colour cannot be known from the styles.
      if (ps.backgroundImage !== 'none') { found.push({ z: -1, c: null }); return; }
      if (!(z < 0)) return;
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
  function hasTexture(n) {
    return ['::before', '::after'].some(function (which) { var ps = getComputedStyle(n, which); return ps && ps.content !== 'none' && ps.backgroundImage !== 'none'; });
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
      if (c[3] === 0 || cs.isolation === 'isolate' || cs.zIndex !== 'auto' || hasTexture(n)) {
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
  // Text whose background is a picture, a gradient or see-through: its colours cannot be read from the styles.
  // blueprint.py measures these from a picture of the page; the viewer can only count them.
  var unmeasuredEls = [];
  function contrastIssues() {
    var groups = {}, seen = [], count = 0;
    unmeasuredEls = [];
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
      if (fg && !bg && fg[3] > 0) unmeasuredEls.push({ el: p, color: fg, sample: text.slice(0, 40),
        required: parseFloat(cs.fontSize) >= 24 || (parseFloat(cs.fontSize) >= 18.66 && parseInt(cs.fontWeight, 10) >= 700) ? 3 : 4.5 });
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
    neverLoaded: neverLoaded, contrastIssues: contrastIssues, unmeasured: function () { return unmeasuredEls; },
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
        unmeasured: unmeasuredEls.map(function (u) { return { color: hex(u.color), sample: u.sample, required: u.required }; }),
        anchorsOnPage: Object.keys(found),
        anchorsNotDescribed: Object.keys(found).filter(function (id) { return !described[id]; })
      };
    }
  };
})();
