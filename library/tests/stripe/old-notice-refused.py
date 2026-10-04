"""A correctly signed notice is refused once it is more than five minutes old, unless the tolerance is changed."""
from _notice import SECRET, notice, report
import stripe


def check(seconds_ago, **options):
    body, header = notice(seconds_ago)
    try:
        stripe.Webhook.construct_event(body, header, SECRET, **options)
        return "accepted"
    except Exception as e:   # noqa: BLE001
        return "REFUSED: " + type(e).__name__


fresh, stale, allowed = check(10), check(600), check(600, tolerance=3600)
report(fresh == "accepted" and stale.startswith("REFUSED") and allowed == "accepted",
       f"stripe library {stripe.VERSION}: a notice signed 10 seconds ago was {fresh}; one signed 10 minutes ago was {stale}; the same with tolerance=3600 was {allowed}")
