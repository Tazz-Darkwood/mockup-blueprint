/* Runs before the page's own scripts: notes which kind of drawing context each canvas asks for, so canvas.js can tell a 3D scene from a 2D chart.
   Read and evaluated by blueprint.py; not copied into mockups. */
(() => {
  const real = HTMLCanvasElement.prototype.getContext;
  HTMLCanvasElement.prototype.getContext = function (kind, ...rest) {
    const ctx = real.call(this, kind, ...rest);
    if (ctx && !this.__bpKind) this.__bpKind = kind;
    return ctx;
  };
})()
