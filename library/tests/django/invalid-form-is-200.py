"""The usual form view answers a mistake with status 200 and the form again, not an error status."""
from _setup import report, setup
version = setup()
from django import forms
from django.http import HttpResponse
from django.test import Client
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


class SignUp(forms.Form):
    email = forms.EmailField()


@csrf_exempt
def signup(request):
    form = SignUp(request.POST or None)
    if request.method == "POST" and form.is_valid():
        return HttpResponse("thanks")
    return HttpResponse(form.as_p())   # what render(request, template, {"form": form}) does: status 200


urlpatterns = [path("signup/", signup)]
reply = Client().post("/signup/", {"email": "not-an-address"})
body = reply.content.decode()
report(reply.status_code == 200 and "Enter a valid email address" in body,
       f"Django {version}: a form sent with a bad email came back with status {reply.status_code} and the message "
       f"{'Enter a valid email address' if 'Enter a valid email address' in body else 'MISSING'} in the page")
