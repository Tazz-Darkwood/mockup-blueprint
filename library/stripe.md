---
name: Stripe Checkout
summary: Payment service where the buyer pays on Stripe's own page and Stripe then tells the site's server. Read when a blueprint takes real money through Stripe. What the server must do with payment notices (check them, apply each once, cope with repeats and wrong order), and what to settle before selling anything.
detect: ["\\bstripe\\b", "checkout\\.session", "whsec_"]
version: 16.0.0
needs: stripe
checked: 2026-10-03
source: https://docs.stripe.com/webhooks and https://docs.stripe.com/checkout/fulfillment (read 2026-10-03); the two approved notes are tests of Stripe's official Python library, version 16.0.0
---

# Stripe Checkout

With Checkout the buyer leaves the site, pays on a page Stripe hosts, and comes back. Card details never touch the site. Stripe then sends the site's server a notice (a webhook) saying what happened, and the server gives the buyer what they paid for.

A mockup shows a "Buy" button and a "Thank you" page. Everything that matters happens between those two and none of it is visible: the notice, the checking, the giving. So for a site that takes money the blueprint has to describe the server's side of each payment, and what happens when a payment is later refunded or disputed.

Only the first two notes below are tested here, with Stripe's own library and a made-up secret. The rest are drafts taken from Stripe's documentation on the date above: they need a real Stripe test account to confirm.

## Use it properly

For the blueprint:

- For each thing sold: what it is, its price, and exactly what the buyer's account gains.
- A route that receives Stripe's notices, with what it does for each kind of notice it listens to. At the least: paid, paid later, refunded, disputed.
- What identifies a payment so it is applied once (Stripe's event id and the Checkout Session id).
- What the game takes back when a payment is refunded or disputed, and what happens if it has already been spent or traded.
- The secrets: the secret key and the signing secret for notices, named in `deployment.secrets`, never written down. Test-mode keys only on a developer's machine.

## Notes

### The signature is over the exact bytes Stripe sent
- Status: approved
- Test: `tests/stripe/signature-needs-exact-body.py` (passed 2026-10-03, stripe library 16.0.0)
- What happens: `stripe.Webhook.construct_event(body, header, secret)` accepted a notice given the exact body and its `Stripe-Signature` header. The same data, read as JSON and written out again, was refused with `SignatureVerificationError`. So was the exact body checked with a different secret.
- What to do: hand the library the raw request body, untouched. In Django that is `request.body`, not `request.POST` and not `json.loads(...)` written back out. Check the signature before doing anything else with the notice, and answer 400 when it fails.
- Why it matters: without this check anyone who finds the address can send a made-up "paid" notice and be given the goods.

### A correctly signed notice is refused once it is more than five minutes old
- Status: approved
- Test: `tests/stripe/old-notice-refused.py` (passed 2026-10-03, stripe library 16.0.0)
- What happens: a notice signed 10 seconds earlier was accepted. One signed 10 minutes earlier was refused. With `tolerance=3600` the older one was accepted.
- What to do: leave the tolerance alone; it stops a captured notice being sent again later. It does mean the server's clock has to be right. When replaying saved notices in development, sign them afresh.

### The notice route cannot have Django's forged-request check
- Status: draft
- Test: none here for the pair. `tests/django/csrf-refuses-post.py` shows Django refusing any POST without its token, and Stripe's notices carry none.
- Source: Stripe's webhook documentation, "Exempt webhook route from CSRF protection".
- What to do: mark that one view `@csrf_exempt`. It is safe to do so only because the signature check takes the place of the token, so the two go together: a view that is exempt and does not check the signature is open to anyone.

### The same notice can arrive more than once, and notices can arrive out of order
- Status: draft
- Test: none. Needs a Stripe test account. `tests/django/idempotency-key.py` tests the defence.
- Source: Stripe's webhook documentation: "Webhook endpoints might occasionally receive the same event more than once", "Stripe doesn't guarantee the delivery of events in the order that they're generated", and its fulfilment guide: the fulfilment function "might be called multiple times, possibly concurrently, for the same Checkout Session".
- What to do: record each event id, and each Checkout Session id that has been fulfilled, in a column marked unique, in the same transaction that grants the goods (see "A unique key on each action" in `django.md`). Do not rely on the order of arrival: when a notice refers to something not yet seen, fetch it from Stripe.

### Answer quickly, and do the work after
- Status: draft
- Test: none. Needs a Stripe test account.
- Source: Stripe's webhook documentation: the route "must quickly return a successful status code (2xx) before any complex logic that could cause a timeout"; undelivered notices are retried "for up to three days with an exponential back off"; and with a success page set, "Checkout waits up to 10 seconds for your server to respond" before sending the buyer back.
- What to do: check the signature, record the event, answer 200. Keep the granting short and inside one transaction; anything slow (email, pictures) goes after.

### The thank-you page is not proof of payment
- Status: draft
- Test: none. Needs a Stripe test account.
- Source: Stripe's fulfilment guide: "You can't rely on triggering fulfillment only from your checkout landing page, because it's not guaranteed customers visit that page." Some payment methods finish later, and then the notice to wait for is `checkout.session.async_payment_succeeded`.
- What to do: grant from the notice. The return page may also try, using the same function and the same once-only record, so a buyer who is still there sees their goods at once. Before granting, check the session's `payment_status` is not `unpaid`.

### Tying a payment to an account
- Status: draft
- Test: none. Needs a Stripe test account.
- Source: Stripe's API reference for Checkout Sessions (`client_reference_id` and `metadata`); not on the two pages read today.
- What to do: when the server creates the Checkout Session it puts its own account id on it, and reads it back from the notice. Never take the account from anything the browser sends on the way back.

### Refunds and disputes are notices too
- Status: draft
- Test: none. Needs a Stripe test account and a decision from the owner.
- Source: the research document for the game this page was written for; Stripe's event list was not read today.
- What to do: listen for refund and dispute notices and decide in the blueprint what the game does: take the goods back, hold a newly bought currency untradeable for some days so it can be taken back, and never punish an account automatically for a dispute.

### Trying notices on a developer's machine
- Status: draft
- Test: none. Needs the Stripe command-line tool and a test account.
- Source: Stripe's webhook documentation: `stripe listen --forward-to localhost:4242/webhook` forwards notices to a local server and prints the signing secret to use; `stripe trigger checkout.session.completed` sends a sample.
- What to do: use it with test-mode keys only. The secret it prints is for that session and differs from the live one.

## What the skill cannot check

- Anything about a real Stripe account, or whether a built site handles notices correctly.
- Whether what is being sold is allowed. Stripe restricts some kinds of business; read its list and describe the business accurately when signing up.
- Law and tax. See "Selling things for real money" in `references/gap-checklist.md`: those are questions for a lawyer and an accountant, and they block the launch.

## Questions it raises

- What exactly is sold, and can it be traded or given away once bought?
- What does the game do when a payment is refunded or disputed after the goods were used?
- Who is the seller on the receipt, and who handles sales tax?
- Has a lawyer been asked whether the in-game currency or any random reward raises legal questions?
