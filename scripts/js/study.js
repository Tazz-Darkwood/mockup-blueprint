/* Measures the first screen of a site someone admires, for writing a style guide from: type sizes, typefaces, colours, pictures.
   Read and evaluated by blueprint.py; not copied into mockups. */
(() => {
  const H = innerHeight, W = innerWidth;
  const inView = e => { const r = e.getBoundingClientRect(); return r.width > 4 && r.height > 4 && r.top < H && r.bottom > 0 && r.left < W && r.right > 0
    && (!e.checkVisibility || e.checkVisibility({ checkOpacity: true, checkVisibilityCSS: true })); };   // not labels hidden for screen readers only
  const els = [...document.querySelectorAll('body *')].filter(inView);
  const words = e => (e.innerText || '').trim().replace(/\s+/g, ' ');
  const texts = els.filter(e => [...e.childNodes].some(n => n.nodeType === 3 && n.nodeValue.trim().length > 1));
  const sizes = texts.map(e => Math.round(parseFloat(getComputedStyle(e).fontSize)));
  const family = e => getComputedStyle(e).fontFamily.split(',')[0].replace(/["']/g, '').trim();
  const count = list => { const m = {}; list.forEach(x => m[x] = (m[x] || 0) + 1); return Object.entries(m).sort((a, b) => b[1] - a[1]).map(x => x[0]); };
  const biggest = texts.slice().sort((a, b) => parseFloat(getComputedStyle(b).fontSize) - parseFloat(getComputedStyle(a).fontSize))[0];
  const area = {};
  els.forEach(e => { const c = getComputedStyle(e).backgroundColor; if (c === 'rgba(0, 0, 0, 0)' || c === 'transparent') return;
    const r = e.getBoundingClientRect(); const a = Math.max(0, Math.min(r.right, W) - Math.max(r.left, 0)) * Math.max(0, Math.min(r.bottom, H) - Math.max(r.top, 0)); area[c] = (area[c] || 0) + a; });
  const shownArea = e => { const r = e.getBoundingClientRect(); return Math.max(0, Math.min(r.right, W) - Math.max(r.left, 0)) * Math.max(0, Math.min(r.bottom, H) - Math.max(r.top, 0)); };
  const pics = els.filter(e => { const r = e.getBoundingClientRect(); if (r.width < 160 || r.height < 120) return false;
    return /^(IMG|VIDEO|CANVAS|PICTURE)$/.test(e.tagName) || (e.tagName.toLowerCase() === 'svg') || getComputedStyle(e).backgroundImage.includes('url('); });
  const pictures = pics.length, pictureShare = Math.round(100 * Math.min(1, Math.max(0, ...pics.map(shownArea)) / (W * H)));
  // a box laid over the page: fixed or sticky, of some size, and talking about cookies, newsletters or offers
  const boxes = els.filter(e => { const p = getComputedStyle(e).position; if (p !== 'fixed' && p !== 'sticky') return false;
    return shownArea(e) > W * H * 0.04 && /cookie|consent|privacy|subscrib|newsletter|sign up|% off|your email/i.test(words(e)); });
  const box = boxes.sort((a, b) => shownArea(b) - shownArea(a))[0];
  const all = words(document.body);
  const blocked = /access (to this (content|page) )?(has been |is )?(denied|restricted)|verify (you are|the security)|unusual traffic|are you a robot|captcha|error\s?(40\d|410|50\d)|page not found|site can.t be reached/i.test(document.title + ' ' + all.slice(0, 600));
  const filled = [...document.querySelectorAll('a, button')].filter(e => { if (!inView(e)) return false; const bg = getComputedStyle(e).backgroundColor; const s = e.innerText.trim();
    return bg !== 'rgba(0, 0, 0, 0)' && bg !== 'transparent' && s.length > 1 && s.length < 40 && e.getBoundingClientRect().height < 90; }).map(e => e.innerText.trim().replace(/\s+/g, ' ')).slice(0, 5);
  const nav = document.querySelector('header nav, nav'), h1 = document.querySelector('h1');
  return { title: document.title.slice(0, 80), largestText: sizes.length ? Math.max(...sizes) : null, largestTextSays: biggest ? words(biggest).slice(0, 60) : null,
    largestTextFace: biggest ? family(biggest) : null, readingText: Math.round(parseFloat(getComputedStyle(document.body).fontSize)), sizesInFirstScreen: new Set(sizes).size,
    faces: count(texts.map(family)).slice(0, 4), headline: h1 && words(h1) && !/[<>]/.test(words(h1)) ? words(h1).slice(0, 90) : null,
    filledButtons: filled, menuLinks: nav ? [...nav.querySelectorAll('a')].filter(a => a.getClientRects().length).length : null,
    pageColour: getComputedStyle(document.body).backgroundColor, biggestColourAreas: Object.entries(area).sort((a, b) => b[1] - a[1]).slice(0, 4).map(x => x[0]),
    picturesInFirstScreen: pictures, biggestPictureShare: pictureShare, boxOnTop: box ? words(box).slice(0, 70) : null, wordsOnPage: all.length, looksBlocked: blocked };
})()
