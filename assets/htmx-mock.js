/* htmx-mock.js: a pretend server for HTMX mockups.

   HTMX fetches pieces of a page from a server. A mockup opened from a folder has no server, and the
   browser refuses to fetch files beside the page. This script answers HTMX's requests itself, from
   functions written in the mockup, so the mockup behaves as the real site will.

   Use: copy this file beside the mockup's pages, load it after htmx, and describe the server:

       <script src="htmx-mock.js"></script>
       <script>
         htmxMock({
           'GET /search': (asked) => '<li>Results for ' + htmxMock.escape(asked.params.q) + '</li>',
           'POST /items': (asked) => asked.params.name ? '<li>' + htmxMock.escape(asked.params.name) + '</li>'
                                                        : { status: 422, body: '<p class="error">Give it a name.</p>' },
         }, { delay: 300 });
       </script>

   An address may have changing parts: 'POST /sessions/:id/signup' matches /sessions/7/signup and gives
   asked.params.id as '7'. Each function is given { method, path, params, headers } and returns the HTML to send back, or
   { status, body, headers } for anything other than a plain success. A request nothing matches
   gets a 404 that says so. Anything a visitor typed goes through htmxMock.escape() before it is put
   into a reply, as the real server must do, or it can run as script. It is mockup tooling: the real
   site has a real server, and every route written here is a route the blueprint must describe. */
(function () {
  window.htmxMock = function (routes, options) {
    var delay = (options && options.delay) || 0, log = [];
    function Fake() { this.headers = {}; this.upload = { addEventListener: function () {} }; this.readyState = 0; this.status = 0; this.response = this.responseText = ''; }
    Fake.prototype.open = function (method, url) { this.method = String(method).toUpperCase(); this.url = url; this.responseURL = new URL(url, location.href).href; };
    Fake.prototype.setRequestHeader = function (name, value) { this.headers[name] = value; };
    Fake.prototype.overrideMimeType = function () {};
    Fake.prototype.addEventListener = function (name, fn) { (this['_' + name] = this['_' + name] || []).push(fn); };
    Fake.prototype.getResponseHeader = function (name) { var all = this.replyHeaders || {}; for (var key in all) if (key.toLowerCase() === String(name).toLowerCase()) return all[key]; return null; };
    Fake.prototype.getAllResponseHeaders = function () { var all = this.replyHeaders || {}, text = ''; for (var key in all) text += key + ': ' + all[key] + '\r\n'; return text; };
    Fake.prototype.abort = function () { this.aborted = true; if (this.onabort) this.onabort(); };
    Fake.prototype.send = function (body) {
      var xhr = this, where = new URL(this.url, location.href), params = {};
      where.searchParams.forEach(function (value, name) { params[name] = value; });
      if (body instanceof FormData) body.forEach(function (value, name) { params[name] = value; });
      else if (typeof body === 'string') new URLSearchParams(body).forEach(function (value, name) { params[name] = value; });
      // the address as written (without what follows "?"), and matched against routes that may have changing parts: 'POST /sessions/:id/signup/'
      var written = this.url.split('?')[0], path = written.charAt(0) === '/' ? written : '/' + written.replace(/^\.?\//, ''), route = null, method = this.method;
      Object.keys(routes).some(function (key) {
        var at = key.indexOf(' '), names = [];
        if (key.slice(0, at).toUpperCase() !== method) return false;
        var pattern = key.slice(at + 1).trim().replace(/[.*+?^${}()|[\]\\]/g, '\\$&').replace(/:(\w+)/g, function (all, name) { names.push(name); return '([^/]+)'; });
        var found = new RegExp('^' + pattern + '$').exec(path) || new RegExp('^' + pattern + '$').exec(written);
        if (!found) return false;
        names.forEach(function (name, i) { params[name] = decodeURIComponent(found[i + 1]); });
        route = routes[key]; return true;
      });
      var asked = { method: this.method, path: path, params: params, headers: this.headers };
      log.push(asked);
      setTimeout(function () {
        if (xhr.aborted) return;
        var reply = route ? route(asked) : { status: 404, body: 'htmx-mock: nothing answers ' + asked.method + ' ' + path };
        if (typeof reply === 'string') reply = { status: 200, body: reply };
        xhr.status = reply.status || 200; xhr.statusText = String(xhr.status); xhr.response = xhr.responseText = reply.body || ''; xhr.replyHeaders = reply.headers || {}; xhr.readyState = 4;
        if (xhr.onload) xhr.onload();
        (xhr._loadend || []).forEach(function (fn) { fn({ lengthComputable: false }); });
      }, delay);
    };
    window.XMLHttpRequest = Fake;
    return { requests: log };
  };
  window.htmxMock.escape = function (text) {
    return String(text == null ? '' : text).replace(/[&<>"']/g, function (c) { return '&#' + c.charCodeAt(0) + ';'; });
  };
})();
