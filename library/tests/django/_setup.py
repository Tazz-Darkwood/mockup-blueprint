"""Shared by the Django test scripts: a configured Django, a throwaway Postgres when asked for, and a way to report.

Each test is one small script. It ends by calling report(passed, detail), which prints one line of JSON for the
runner (blueprint.py library --test django) and for a person running the script by hand."""
import atexit
import json
import sys
import tempfile
import threading


def report(passed, detail):
    print(json.dumps({"pass": bool(passed), "detail": str(detail)}))
    sys.stdout.flush()
    sys.exit(0)


def setup(database="sqlite", urls=None, **extra):
    """Configure Django for one script. database is "sqlite" or "postgres" (a real server, started for this script and thrown away)."""
    import django
    from django.conf import settings
    if database == "postgres":
        import pgserver
        folder = tempfile.mkdtemp(prefix="bp-pg-")
        server = pgserver.get_server(folder, cleanup_mode="delete")
        atexit.register(server.cleanup)
        from psycopg.conninfo import conninfo_to_dict
        where = conninfo_to_dict(server.get_uri())   # a socket folder on Linux and macOS; an address and a port on Windows
        db = {"ENGINE": "django.db.backends.postgresql", "NAME": where.get("dbname", "postgres"), "USER": where.get("user", "postgres"),
              "PASSWORD": where.get("password") or "", "HOST": where.get("host", folder), "PORT": str(where.get("port") or "")}
    else:
        db = {"ENGINE": "django.db.backends.sqlite3", "NAME": tempfile.mkdtemp(prefix="bp-sqlite-") + "/db.sqlite3"}
    conf = dict(
        SECRET_KEY="for-tests-only", DATABASES={"default": db}, USE_TZ=True, ALLOWED_HOSTS=["testserver"],
        INSTALLED_APPS=["django.contrib.contenttypes", "django.contrib.auth", "django.contrib.sessions"],
        MIDDLEWARE=["django.contrib.sessions.middleware.SessionMiddleware", "django.middleware.csrf.CsrfViewMiddleware",
                    "django.contrib.auth.middleware.AuthenticationMiddleware"],
        TEMPLATES=[{"BACKEND": "django.template.backends.django.DjangoTemplates", "APP_DIRS": True,
                    "OPTIONS": {"context_processors": ["django.template.context_processors.request"]}}],
        ROOT_URLCONF=urls or "__main__",
    )
    conf.update(extra)
    settings.configure(**conf)
    django.setup()
    return django.get_version()


def tables(*models):
    """Create the tables for models defined in the script, and for sign-in and sessions."""
    from django.core.management import call_command
    from django.db import connection
    call_command("migrate", verbosity=0, interactive=False)
    with connection.schema_editor() as editor:
        for model in models:
            editor.create_model(model)


def together(*jobs):
    """Run the jobs at the same moment, each on its own database connection, as two requests arriving together would.
    Returns what each returned, or the exception it raised."""
    from django.db import connection
    results = [None] * len(jobs)
    start = threading.Barrier(len(jobs))

    def run(i, job):
        try:
            start.wait(timeout=10)
            results[i] = job()
        except Exception as e:   # noqa: BLE001 - the test wants to see whatever happened
            results[i] = e
        finally:
            connection.close()

    threads = [threading.Thread(target=run, args=(i, job)) for i, job in enumerate(jobs)]
    for t in threads:
        t.start()
    for t in threads:
        t.join(timeout=60)
    return results
