/* Runs before the page's own scripts: makes 3D contexts unavailable, to see what a visitor without 3D gets.
   Read and evaluated by blueprint.py; not copied into mockups. */
(() => {
  const real = HTMLCanvasElement.prototype.getContext;
  HTMLCanvasElement.prototype.getContext = function (kind, ...rest) { return /webgl/.test(kind) ? null : real.call(this, kind, ...rest); };
})()
