"""The signature is over the exact bytes Stripe sent: a body that was read as JSON and written out again fails."""
import json
from _notice import SECRET, notice, report
import stripe

body, header = notice()
try:
    event = stripe.Webhook.construct_event(body, header, SECRET)
    exact = "accepted, type " + event["type"]
except Exception as e:   # noqa: BLE001
    exact = "REFUSED: " + type(e).__name__
rewritten = json.dumps(json.loads(body), indent=2)        # what a framework that parses the body and re-serialises it would hand over
try:
    stripe.Webhook.construct_event(rewritten, header, SECRET)
    again = "accepted"
except Exception as e:   # noqa: BLE001
    again = "REFUSED: " + type(e).__name__
try:
    stripe.Webhook.construct_event(body, header, "whsec_some_other_secret")
    wrong = "accepted"
except Exception as e:   # noqa: BLE001
    wrong = "REFUSED: " + type(e).__name__
report(exact.startswith("accepted") and again.startswith("REFUSED") and wrong.startswith("REFUSED"),
       f"stripe library {stripe.VERSION}: the exact body with its header was {exact}; the same data parsed and written out again was {again}; the exact body checked with another secret was {wrong}")
