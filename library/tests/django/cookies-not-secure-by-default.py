"""Out of the box the sign-in and CSRF cookies are not marked Secure; the CSRF cookie can be read by scripts, the session cookie cannot."""
from _setup import report, setup
version = setup()
from django.conf import settings

seen = {k: getattr(settings, k) for k in ("SESSION_COOKIE_SECURE", "CSRF_COOKIE_SECURE", "SESSION_COOKIE_HTTPONLY", "CSRF_COOKIE_HTTPONLY",
                                          "SESSION_COOKIE_SAMESITE", "CSRF_COOKIE_SAMESITE")}
report(seen == {"SESSION_COOKIE_SECURE": False, "CSRF_COOKIE_SECURE": False, "SESSION_COOKIE_HTTPONLY": True, "CSRF_COOKIE_HTTPONLY": False,
                "SESSION_COOKIE_SAMESITE": "Lax", "CSRF_COOKIE_SAMESITE": "Lax"},
       f"Django {version} defaults: " + ", ".join(f"{k} = {v}" for k, v in seen.items()))
