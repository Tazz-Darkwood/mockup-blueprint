"""Two requests that read a balance, work on it and save it lose one of the changes, unless the row is locked."""
import time
from _setup import report, setup, tables, together
version = setup("postgres")
from django.db import models, transaction


class Wallet(models.Model):
    coins = models.IntegerField()

    class Meta:
        app_label = "game"


tables(Wallet)
wallet = Wallet.objects.create(coins=100)


def spend(lock):
    def job():
        with transaction.atomic():
            rows = Wallet.objects.select_for_update() if lock else Wallet.objects
            w = rows.get(pk=wallet.pk)
            time.sleep(0.3)        # the request is busy: checking a price, rolling a result
            w.coins -= 10
            w.save()
    return job


together(spend(False), spend(False))
unlocked = Wallet.objects.get(pk=wallet.pk).coins
Wallet.objects.update(coins=100)
together(spend(True), spend(True))
locked = Wallet.objects.get(pk=wallet.pk).coins
report(unlocked == 90 and locked == 80,
       f"Django {version} on Postgres: two purchases of 10 coins made at the same moment from 100 left {unlocked} (one purchase was free); "
       f"with select_for_update() on the read they left {locked}")
