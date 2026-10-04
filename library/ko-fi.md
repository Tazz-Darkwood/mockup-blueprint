---
name: Ko-fi
summary: Tipping and membership page that can notify a site's server when someone pays. Read when a blueprint takes support through Ko-fi. Every note here is second-hand and unconfirmed. In short, it suits thanks and perks that cannot be traded, and does not suit selling anything of value.
detect: ["ko-fi", "\\bkofi\\b"]
checked: 2026-10-03
source: second-hand. Ko-fi's own help pages refused to load on 2026-10-03 (the server answered 403). The notes come from a research document supplied by a user, which cites Ko-fi's help centre and a public description of its webhook fields.
---

# Ko-fi

Ko-fi gives a creator a page where people can leave a tip, join a membership or buy from a small shop. It can send a notice to a server address of the creator's choosing each time a payment is made.

Nothing on this page has been tested or read at first hand. Treat every note as a lead to check against Ko-fi's own documentation and with a real test payment before anything is built on it.

## Use it properly

- Use Ko-fi for support and for perks that cannot be traded or sold on: a badge, a cosmetic, a time-limited benefit that each payment extends.
- Do not use it to sell anything with value inside a game economy (a currency, a tradeable item). The notes below say why.
- In wording, say "support" and describe what the money is for. Avoid "donation" unless the organisation is a registered charity.

## Notes

### The notice is checked by a fixed token in its body, not by a signature
- Status: draft
- Test: none. Needs a Ko-fi account and a real or test payment.
- What is said to happen: each notice carries a verification token that is the same every time, inside the data itself. There is no signature over the contents.
- What to do if so: compare the token on every notice, keep the address of the route private, and treat the token as a secret. Anyone who learns it can send made-up payments, which is one more reason to grant nothing of value from a Ko-fi notice.
- What would confirm it: Ko-fi's webhook page read at first hand, and a test notice.

### There is no documented way to attach the site's own account to a payment
- Status: draft
- Test: none. Needs a Ko-fi account.
- What is said to happen: a payment arrives with the supporter's name, email and message as they typed them on Ko-fi, with nothing that says which account on the site it is for.
- What to do if so: give each signed-in player a one-time code to paste into the Ko-fi message, match on that, and keep a list of payments that matched nothing for a person to sort out by hand.
- For the blueprint: that list is a screen somebody has to look at. Say who.

### No notice for refunds or disputes was found
- Status: draft
- Test: none.
- What is said to happen: the documented notices cover payments. Nothing was found for a refund or a disputed charge.
- What to do if so: assume the site never hears that money was taken back. Grant only things that cost nothing to lose: time-limited perks, not goods.

### Trying it on a developer's machine
- Status: draft
- Test: none.
- What is said to happen: Ko-fi has a button that sends a sample notice to the address given, and no tool for replaying real ones. The address must be reachable from the internet.
- What to do if so: save sample notices and replay them from a script during development; use a temporary tunnel to receive Ko-fi's own sample.

## Questions it raises

- What does a supporter get, and can it be traded or sold on?
- How is a payment matched to an account, and who deals with the ones that do not match?
- What happens to a perk when support stops?
