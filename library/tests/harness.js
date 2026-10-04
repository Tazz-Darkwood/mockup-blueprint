/* Shared helpers for library test pages.
   A test page calls run(async () => ({ pass, detail })). The result is left on window.libraryResult
   for the test runner, and written onto the page so a person opening the file sees PASS or FAIL. */
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
const $ = (selector) => document.querySelector(selector);

// Wait until the named custom elements are registered (or 10 seconds pass), then let them render.
async function defined(...tags) {
  await Promise.all(tags.map((tag) => Promise.race([customElements.whenDefined(tag), sleep(10000)])));
  await sleep(600);
}

// What a form would send, as "name=value" strings in order.
const formEntries = (form) => [...new FormData(form).entries()].map(([name, value]) => name + '=' + value);

// Is the element taking up space on the page?
const visible = (el) => !!el && el.getClientRects().length > 0 && el.getBoundingClientRect().height > 0;

// The element that really has keyboard focus, looking inside components.
function focused() {
  let el = document.activeElement;
  while (el && el.shadowRoot && el.shadowRoot.activeElement) el = el.shadowRoot.activeElement;
  return el;
}

/* Real mouse and keyboard input. Events faked by script do not behave like a person's (a select
   option does not select, Enter does not submit), so tests that need a person ask the test runner:
     await real('click', '#save')     await real('hover', '#help')    await real('mouse', '5,5')
     await real('type', 'hello')      await real('press', 'Enter')
     await real('aria', '#field')     returns the accessibility tree of that element as text
     await real('drag', '10,10,90,40')   press at the first point, move to the second, release
     await real('wheel', '50,50,300')    turn the mouse wheel 300 pixels with the pointer at 50,50
     await real('swipe', '50,50,-200')   a finger put down at 50,50 and moved 200 pixels up
     await real('motion', 'reduce')      the visitor's device asks for less motion ('no-preference' undoes it)
   The runner polls __realNext, performs the action in the browser, and answers through __realDone. */
const realRequests = [], realWaiting = {};
let realCount = 0;
window.__realNext = () => realRequests.shift() || null;
window.__realDone = (id, value) => { realWaiting[id](value); delete realWaiting[id]; };
function real(action, arg) {
  if (!window.__libraryRunner) {
    return Promise.reject(new Error('needs real mouse and keyboard input, which only the test runner gives: run "blueprint.py library --test"'));
  }
  return new Promise((resolve, reject) => {
    const id = ++realCount;
    realWaiting[id] = (value) => (typeof value === 'string' && value.startsWith('ERROR ') ? reject(new Error(value)) : resolve(value));
    realRequests.push({ id, action, arg });
  });
}

function run(test) {
  (async () => {
    try {
      const result = await test();
      return { pass: !!result.pass, detail: String(result.detail || '') };
    } catch (error) {
      return { pass: false, detail: 'threw: ' + ((error && error.message) || error) };
    }
  })().then((result) => {
    window.libraryResult = result;
    const line = document.createElement('pre');
    line.textContent = (result.pass ? 'PASS: ' : 'FAIL: ') + result.detail;
    line.style.cssText = 'opacity:1;padding:8px;white-space:pre-wrap;border:2px solid ' + (result.pass ? 'green' : 'red');
    document.documentElement.appendChild(line);
  });
}
