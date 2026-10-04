/* Shared by the PixiJS test pages. Loaded as a plain script, which works when a page is opened from a folder. */
// A 64 by 64 picture as a data address: the left half white, the right half mid-grey (128).
const GREY = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAZklEQVR4nO3QgQkAAAjDME/f53rGEFLoA5ktl6T6AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP8BDhR/2v42L3phAAAAAElFTkSuQmCC";
const frames = (n) => new Promise((done) => { const step = () => (n-- > 0 ? requestAnimationFrame(step) : done()); step(); });
// Colour of one pixel of what was just drawn, read straight from the graphics card. x and y count from the top left.
function glPixel(app, x, y) {
  const gl = app.renderer.gl, p = new Uint8Array(4);
  gl.readPixels(x, app.canvas.height - 1 - y, 1, 1, gl.RGBA, gl.UNSIGNED_BYTE, p);
  return [...p];
}
// Colour of one pixel of the canvas as a saved picture would have it (canvas.toDataURL).
async function savedPixel(canvas, x, y) {
  const picture = new Image();
  picture.src = canvas.toDataURL();
  await new Promise((done) => { picture.onload = done; });
  const copy = document.createElement('canvas');
  copy.width = canvas.width; copy.height = canvas.height;
  const pen = copy.getContext('2d');
  pen.drawImage(picture, 0, 0);
  return [...pen.getImageData(x, y, 1, 1).data];
}
async function stage(options) {
  const app = new PIXI.Application();
  await app.init(Object.assign({ width: 300, height: 200, background: '#102030' }, options || {}));
  document.body.appendChild(app.canvas);
  return app;
}
