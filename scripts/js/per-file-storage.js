/* Runs before the page's own scripts: gives every file its own separate storage, as some browsers do for pages opened from a folder.
   Read and evaluated by blueprint.py; not copied into mockups. */
(() => {
  const real = window.localStorage, get = Storage.prototype.getItem, set = Storage.prototype.setItem, slot = '__per_file__' + location.pathname;
  let data = {}; try { data = JSON.parse(get.call(real, slot) || '{}'); } catch (e) {}
  const flush = () => { try { set.call(real, slot, JSON.stringify(data)); } catch (e) {} };
  window.__firstReads = {};
  const fake = {
    getItem: (k) => { const v = k in data ? data[k] : null; if (!(k in window.__firstReads)) window.__firstReads[k] = v; return v; },
    setItem: (k, v) => { data[k] = String(v); flush(); }, removeItem: (k) => { delete data[k]; flush(); }, clear: () => { data = {}; flush(); },
    key: (i) => { const keys = Object.keys(data); return i < keys.length ? keys[i] : null; }, get length() { return Object.keys(data).length; },
  };
  Object.defineProperty(window, 'localStorage', { value: fake, configurable: true });
})()
