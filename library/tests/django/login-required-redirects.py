"""login_required answers a signed-out visitor with a redirect to the sign-in page, also when the request came from HTMX."""
from _setup import report, setup, tables
version = setup()
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.test import Client
from django.urls import path


@login_required
def tank(request):
    return HttpResponse("your tank")


urlpatterns = [path("tank/", tank)]
tables()
plain = Client().get("/tank/")
from_htmx = Client().get("/tank/", headers={"HX-Request": "true"})
report(plain.status_code == 302 and plain["Location"] == "/accounts/login/?next=/tank/" and from_htmx.status_code == 302,
       f"Django {version}: a signed-out request for /tank/ got {plain.status_code} to {plain['Location']}; the same request sent by HTMX got {from_htmx.status_code} to {from_htmx['Location']}, "
       "which the browser follows by itself, so HTMX is handed the sign-in page as if it were the piece it asked for")
