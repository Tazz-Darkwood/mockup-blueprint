"""A POST with no token is refused; a token in the form or in a header (the HTMX way) is accepted."""
from _setup import report, setup
version = setup()
from django.http import HttpResponse
from django.middleware.csrf import get_token
from django.test import Client
from django.urls import path


def form(request):
    if request.method == "POST":
        return HttpResponse("saved " + request.POST.get("name", ""))
    return HttpResponse("token is " + get_token(request))


urlpatterns = [path("form/", form)]
client = Client(enforce_csrf_checks=True)
token = client.get("/form/").content.decode().split()[-1]
bare = client.post("/form/", {"name": "Ada"}).status_code
in_form = client.post("/form/", {"name": "Ada", "csrfmiddlewaretoken": token}).status_code
in_header = client.post("/form/", {"name": "Ada"}, headers={"X-CSRFToken": token}).status_code
report(bare == 403 and in_form == 200 and in_header == 200,
       f"Django {version}: a POST with no token got {bare}; with the token as a form field {in_form}; with the token in an X-CSRFToken header {in_header}")
