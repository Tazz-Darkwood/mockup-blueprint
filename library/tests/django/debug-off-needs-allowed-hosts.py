"""With DEBUG off, a request for a host name not in ALLOWED_HOSTS is refused with 400, by the middleware a new project has."""
from _setup import report, setup
STARTPROJECT = ["django.middleware.security.SecurityMiddleware", "django.contrib.sessions.middleware.SessionMiddleware", "django.middleware.common.CommonMiddleware",
              "django.middleware.csrf.CsrfViewMiddleware", "django.contrib.auth.middleware.AuthenticationMiddleware",
              "django.middleware.clickjacking.XFrameOptionsMiddleware"]   # what 'startproject' writes
version = setup(DEBUG=False, ALLOWED_HOSTS=["kiln.example"], MIDDLEWARE=STARTPROJECT)
from django.http import HttpResponse
from django.test import Client
from django.urls import path

urlpatterns = [path("", lambda request: HttpResponse("hello"))]
listed = Client().get("/", headers={"host": "kiln.example"}).status_code
other = Client().get("/", headers={"host": "kiln-clay.onrender.com"}).status_code
report(listed == 200 and other == 400,
       f"Django {version}: with ALLOWED_HOSTS = ['kiln.example'] and DEBUG off, a request for kiln.example got {listed} and one for kiln-clay.onrender.com got {other}")
