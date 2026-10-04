/* Given a selector, says whether the element that holds a canvas still shows something when 3D is unavailable.
   Read and evaluated by blueprint.py; not copied into mockups. */
(selector) => {
  const box = document.querySelector(selector);
  if (!box) return null;
  const shown = (e) => { const r = e.getBoundingClientRect(); return r.width > 20 && r.height > 20; };
  return [...box.querySelectorAll('img, svg, picture, video, canvas')].some(shown) || box.innerText.trim().length > 0;
}
