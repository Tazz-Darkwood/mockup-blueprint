"""Shared by the Stripe test scripts: makes a payment notice signed the way Stripe documents, with a made-up secret,
so the official library's checking can be tried with no Stripe account and nothing sent anywhere."""
import hashlib
import hmac
import json
import sys
import time

SECRET = "whsec_made_up_for_tests_only"


def report(passed, detail):
    print(json.dumps({"pass": bool(passed), "detail": str(detail)}))
    sys.exit(0)


def notice(seconds_ago=0, event_id="evt_test_1"):
    """The exact bytes of a notice and its Stripe-Signature header."""
    body = json.dumps({"id": event_id, "object": "event", "type": "checkout.session.completed",
                       "data": {"object": {"id": "cs_test_1", "object": "checkout.session", "payment_status": "paid", "client_reference_id": "player-42"}}},
                      separators=(",", ":"))
    stamp = int(time.time()) - seconds_ago
    signed = hmac.new(SECRET.encode(), f"{stamp}.{body}".encode(), hashlib.sha256).hexdigest()
    return body, f"t={stamp},v1={signed}"
