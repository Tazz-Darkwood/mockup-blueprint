"""On SQLite, select_for_update() is accepted and does nothing: the query is sent with no lock."""
from _setup import report, setup, tables
version = setup("sqlite")
from django.db import connection, models, transaction
from django.test.utils import CaptureQueriesContext


class Wallet(models.Model):
    coins = models.IntegerField()

    class Meta:
        app_label = "game"


tables(Wallet)
Wallet.objects.create(coins=100)
with CaptureQueriesContext(connection) as queries, transaction.atomic():
    Wallet.objects.select_for_update().get(coins=100)
sent = [q["sql"] for q in queries if "game_wallet" in q["sql"]][0]
supported = connection.features.has_select_for_update
report("FOR UPDATE" not in sent.upper() and not supported,
       f"Django {version} on SQLite: select_for_update() raised nothing, the database says it supports row locks: {supported}, "
       f"and the query sent was: {sent[:90]}")
