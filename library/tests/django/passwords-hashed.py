"""create_user stores a salted hash, never the password; a plain .create() stores whatever it is given."""
from _setup import report, setup, tables
version = setup()
from django.contrib.auth.models import User

tables()
good = User.objects.create_user("ada", password="correct horse")
bad = User.objects.create(username="bo", password="correct horse")
report(not good.password.startswith("correct") and good.check_password("correct horse") and bad.password == "correct horse" and not bad.check_password("correct horse"),
       f"Django {version}: create_user stored {good.password.split('$')[0]}$... ({len(good.password)} characters) and check_password accepts the real one; "
       f"User.objects.create(password=...) stored the password itself in the table, and that account cannot sign in")
