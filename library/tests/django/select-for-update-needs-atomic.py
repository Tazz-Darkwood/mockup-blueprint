"""select_for_update() outside a transaction is an error, not a silent no-op, on a database that has row locks."""
from _setup import report, setup, tables
version = setup("postgres")
from django.db import models, transaction


class Wallet(models.Model):
    coins = models.IntegerField()

    class Meta:
        app_label = "game"


tables(Wallet)
Wallet.objects.create(coins=100)
try:
    Wallet.objects.select_for_update().get(coins=100)
    outside = "nothing"
except transaction.TransactionManagementError as e:
    outside = "TransactionManagementError: " + str(e)
with transaction.atomic():
    inside = Wallet.objects.select_for_update().get(coins=100).coins
report(outside.startswith("TransactionManagementError") and inside == 100,
       f"Django {version} on Postgres: select_for_update() with no transaction raised {outside}; inside transaction.atomic it read the row ({inside} coins)")
