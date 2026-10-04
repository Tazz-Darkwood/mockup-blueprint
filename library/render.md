---
name: Render
summary: Hosting that runs servers and databases as well as static sites. Read when a blueprint names it as the host, for service types, secrets and the free-tier limits.
detect: ["onrender\\.com", "render\\.yaml", "render (static site|web service|postgres)", "on render\\b", "\"host\": \"[^\"]*render"]
checked: 2026-10-03
source: https://render.com/docs
---

# Render

Runs a site's server and database, and can also serve static sites. It is the choice when a site needs login, saved data, secrets, email or payments.

Every note here is a draft. They were written from general knowledge and have not been confirmed by a deployment made with this skill. The first real deployment should check each one and record what was seen.

## Use it properly

Confirm with the user which account to use before creating any service. Creating services can cost money and is visible to the world.

## Notes

### Pick the service type to match what the site needs
- Status: draft
- Test: none. Needs a real deployment.
- What happens: Render offers a Static Site for built frontends, a Web Service for a server, and managed Postgres for data.
- What to do: name the service types in the blueprint's `deployment`. Describe the setup in a `render.yaml` in the repository so it can be recreated.

### Secrets go in the service's environment settings
- Status: draft
- Test: none. Needs a real deployment.
- What happens: values set there are available to the server as environment variables and are not in the repository.
- What to do: list the secret names in the blueprint's `deployment.secrets`, never the values. The user supplies the values. Never commit them.

### The server must listen on the port Render provides
- Status: draft
- Test: none. Needs a real deployment.
- What happens: Render passes the port in the `PORT` environment variable. A server listening on a fixed port, or only on localhost, is unreachable.
- What to do: listen on `PORT` and on host `0.0.0.0`. Add a health-check path that answers quickly.

### Free services sleep when idle
- Status: draft
- Test: none. Needs a real deployment.
- What happens: a free web service stops after a period with no visitors and takes a while to wake on the next request. Free databases have limits and an expiry.
- What to do: ask whether the free tier is acceptable. If the blueprint does not say, it is an open question.

### Database changes should run as part of the deploy
- Status: draft
- Test: none. Needs a real deployment.
- What happens: running migrations by hand is forgotten sooner or later, and the deployed code then disagrees with the database.
- What to do: run migrations in the deploy command.

### A Django site needs a production server, its files collected, and its host name allowed
- Status: draft
- Test: none. Needs a real deployment. The settings side is tested in `django.md`.
- What happens: Django's own development server is not for live sites, and with `DEBUG` off Django neither serves its own CSS and scripts nor answers for a host name it has not been told about.
- What to do: start it with a production server (`gunicorn project.wsgi`), run `collectstatic` and the migrations in the build or deploy command, serve the collected files with WhiteNoise, and put both the `.onrender.com` name and any custom domain in `ALLOWED_HOSTS` from the environment.
- What would confirm it: one Django site deployed, with styles loading and forms working.

### Behind Render's proxy, Django must be told the request was secure
- Status: draft
- Test: none. Needs a real deployment.
- What happens: Render ends HTTPS before the request reaches the app, so Django sees plain HTTP. With `SECURE_SSL_REDIRECT` on and nothing else set, every request is redirected for ever.
- What to do: set `SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")`. Only do this behind a proxy that sets that header itself.
- What would confirm it: a deployed site with the redirect on that loads.

### The database address comes from the environment
- Status: draft
- Test: none. Needs a real deployment.
- What happens: a Render Postgres database gives an address containing its password. Render can pass it to the web service as an environment variable.
- What to do: read it from the environment in settings (the `dj-database-url` package parses it). Use a separate database for development; never point a developer's machine at the live one.

## Questions it raises

- Which account will own the services, and who pays if it outgrows the free tier?
- Is a slow first request after a quiet period acceptable?
- Which secrets does the site need, and who holds their values?
