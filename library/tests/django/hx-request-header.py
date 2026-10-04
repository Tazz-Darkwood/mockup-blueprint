"""One view can serve a whole page to a visitor and just the piece to HTMX, by looking at the HX-Request header."""
from _setup import report, setup
version = setup()
from django.http import HttpResponse
from django.test import Client
from django.urls import path


def market(request):
    piece = "<ul id='stalls'><li>Kelp</li></ul>"
    if request.headers.get("HX-Request"):
        return HttpResponse(piece)
    return HttpResponse("<html><body><h1>Market</h1>" + piece + "</body></html>")


urlpatterns = [path("market/", market)]
whole = Client().get("/market/").content.decode()
part = Client().get("/market/", headers={"HX-Request": "true"}).content.decode()
report("<h1>" in whole and "<h1>" not in part and part.startswith("<ul"),
       f"Django {version}: /market/ asked for plainly returned a whole page ({len(whole)} characters, with its heading); asked for with the header HX-Request: true it returned only the list ({len(part)} characters)")
