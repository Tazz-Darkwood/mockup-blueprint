"""A unique key on each action makes a repeated request count once, even when both copies arrive together."""
from _setup import report, setup, tables, together
version = setup("postgres")
from django.db import IntegrityError, models, transaction


class Wallet(models.Model):
    coins = models.IntegerField()

    class Meta:
        app_label = "game"


class Grant(models.Model):
    key = models.CharField(max_length=40, unique=True)   # sent by the browser, or the payment service's event id

    class Meta:
        app_label = "game"


tables(Wallet, Grant)
wallet = Wallet.objects.create(coins=0)


def grant(key):
    def job():
        try:
            with transaction.atomic():
                Grant.objects.create(key=key)                        # fails if this action was already applied
                Wallet.objects.filter(pk=wallet.pk).update(coins=models.F("coins") + 50)
            return "applied"
        except IntegrityError:
            return "already applied"
    return job


outcomes = together(grant("payment-123"), grant("payment-123"), grant("payment-123"))
coins = Wallet.objects.get(pk=wallet.pk).coins
report(coins == 50 and sorted(map(str, outcomes)) == ["already applied", "already applied", "applied"],
       f"Django {version} on Postgres: the same payment notice delivered three times at once gave {coins} coins (50 is one grant); the three attempts ended: {sorted(map(str, outcomes))}")
