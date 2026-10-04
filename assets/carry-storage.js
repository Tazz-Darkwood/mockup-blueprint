/* carry-storage.js: lets the pages of a mockup share the browser's storage when opened from a folder.

   Opened from a folder, some browsers give every file its own separate storage, so what one page
   saves with localStorage another cannot read: a basket empties, a signed-in visitor is signed out,
   on the very next page. This script carries everything in localStorage along whenever the visitor
   moves to another page of the mockup, and puts it back before that page's own scripts run. The
   pages go on using localStorage as usual.

   Use: copy this file beside the mockup's pages and load it first, before any other script:
       <script src="carry-storage.js"></script>
   It is mockup tooling. The real site is served from a host, where storage is shared, and does not
   need it. It must never go live: it lets the address of a link replace what is stored. So it does
   nothing at all unless the page was opened from a folder (file:), and 'audit --launch' reports it.

   How it travels: in the address of links to the mockup's other pages (as "#carry=..."), which is
   removed again on arrival, and in the tab's own name as a second chance where the browser keeps it.
   Scripts that move the visitor themselves should use carryStorage.go('page.html'). A page that saves
   only now and then can listen for the window's 'carry-storage-leaving' event and save when it fires. */
(function () {
  if (location.protocol !== 'file:') {   // served from a host: storage is already shared, and carrying it would be a hole
    window.carryStorage = { link: function (href) { return href; }, go: function (href) { location.href = href; } };
    return;
  }
  var MARK = '#carry=', NAME = 'carry:', STAMP = '__carried_at';
  function unpack(text) { try { return JSON.parse(decodeURIComponent(escape(atob(text)))); } catch (e) { return null; } }
  function everything() {
    var all = {};
    try { for (var i = 0; i < localStorage.length; i++) { var key = localStorage.key(i); if (key !== STAMP) all[key] = localStorage.getItem(key); } } catch (e) { /* storage switched off */ }
    return all;
  }
  function pack() { return btoa(unescape(encodeURIComponent(JSON.stringify({ at: Date.now(), all: everything() })))); }

  // Arriving: take whichever copy is newest, this page's own storage or what was carried here.
  var carried = [], at = location.href.indexOf(MARK);
  if (at >= 0) carried.push(unpack(location.href.slice(at + MARK.length)));
  if (String(window.name).indexOf(NAME) === 0) { carried.push(unpack(window.name.slice(NAME.length))); window.name = ''; }   // read once, then wiped: a site visited later must not find it
  carried = carried.filter(Boolean).sort(function (a, b) { return b.at - a.at; });
  try {
    var mine = Number(localStorage.getItem(STAMP)) || 0;
    if (carried.length && carried[0].at > mine) {
      var have = everything(), bring = carried[0].all, key;
      for (key in have) if (!(key in bring)) localStorage.removeItem(key);   // something was removed on the other page, such as on signing out
      for (key in bring) localStorage.setItem(key, bring[key]);
      localStorage.setItem(STAMP, String(carried[0].at));
    }
  } catch (e) { /* storage switched off: nothing to carry into */ }
  if (at >= 0) {
    try { history.replaceState(null, '', location.href.slice(0, at)); } catch (e) { /* the address just stays long */ }
    // a link to a part of the page ("page.html#prices") still goes there once the page is ready
    var part = location.href.slice(0, at).split('#')[1];
    if (part) document.addEventListener('DOMContentLoaded', function () { var el = document.getElementById(decodeURIComponent(part)); if (el) el.scrollIntoView(); });
  }

  // Leaving: note the time, and put the latest copy where the next page will find it.
  function leave() {
    try { window.dispatchEvent(new Event('carry-storage-leaving')); } catch (e) { /* very old browser */ }   // a page that saves only now and then can listen for this and save first
    try { localStorage.setItem(STAMP, String(Date.now())); } catch (e) { /* storage switched off */ }
  }
  // The tab's name is only filled in on the way to another page of this mockup, never on the way out to another site.
  function link(href) { leave(); try { window.name = NAME + pack(); } catch (e) { /* too much to carry in this browser */ } return href + MARK + pack(); }
  function ownPage(href) { return /^[^:#?\/][^:#?]*\.html?(\?[^#]*)?(#.*)?$/.test(href || ''); }   // a page in this folder or below it, not another site
  function onLink(event) {
    var a = event.target && event.target.closest ? event.target.closest('a[href]') : null;
    if (!a) return;
    var href = a.getAttribute('data-carry-href') || a.getAttribute('href');
    if (!ownPage(href)) return;
    a.setAttribute('data-carry-href', href);
    a.setAttribute('href', link(href));
  }
  document.addEventListener('click', onLink, true);
  document.addEventListener('auxclick', onLink, true);
  document.addEventListener('contextmenu', onLink, true);
  window.addEventListener('pagehide', leave);
  window.carryStorage = { link: link, go: function (href) { location.href = link(href); } };
})();
