/* Runs before the page's own scripts: notes which storage keys each page reads.
   Read and evaluated by blueprint.py; not copied into mockups. */
(() => {
  const get = Storage.prototype.getItem; window.__keysRead = {};
  Storage.prototype.getItem = function (k) { if (this === window.localStorage) window.__keysRead[k] = true; return get.call(this, k); };
})()
