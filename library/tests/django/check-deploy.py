"""'manage.py check --deploy' lists the settings that are unsafe for a live site; a new project has several."""
import io
import re
from _setup import report, setup
STARTPROJECT = ["django.middleware.security.SecurityMiddleware", "django.contrib.sessions.middleware.SessionMiddleware", "django.middleware.common.CommonMiddleware",
                "django.middleware.csrf.CsrfViewMiddleware", "django.contrib.auth.middleware.AuthenticationMiddleware",
                "django.middleware.clickjacking.XFrameOptionsMiddleware"]   # what 'startproject' writes
version = setup(DEBUG=True, MIDDLEWARE=STARTPROJECT)
from django.core.management import call_command

urlpatterns = []
out = io.StringIO()
try:
    call_command("check", deploy=True, stdout=out, stderr=out)
except SystemExit:
    pass
found = sorted(set(re.findall(r"security\.W\d+", out.getvalue())))
wanted = {"security.W004": "SECURE_HSTS_SECONDS", "security.W008": "SECURE_SSL_REDIRECT", "security.W012": "SESSION_COOKIE_SECURE",
          "security.W016": "CSRF_COOKIE_SECURE", "security.W018": "DEBUG"}
report(all(w in found for w in wanted),
       f"Django {version}: check --deploy on settings as a new project has them gave {len(found)} security warnings: {', '.join(found)}. "
       f"Among them: {', '.join(k + ' (' + v + ')' for k, v in wanted.items() if k in found)}")
