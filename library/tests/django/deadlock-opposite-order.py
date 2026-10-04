"""Two trades that lock the same two rows in opposite orders deadlock; locking in one agreed order does not."""
import time
from _setup import report, setup, tables, together
version = setup("postgres")
from django.db import OperationalError, models, transaction


class Wallet(models.Model):
    coins = models.IntegerField()

    class Meta:
        app_label = "game"


tables(Wallet)
a, b = Wallet.objects.create(coins=100), Wallet.objects.create(coins=100)


def trade(first, second, sort):
    def job():
        try:
            with transaction.atomic():
                if sort:
                    list(Wallet.objects.select_for_update().filter(pk__in=[first, second]).order_by("pk"))
                else:
                    Wallet.objects.select_for_update().get(pk=first)
                    time.sleep(0.3)
                    Wallet.objects.select_for_update().get(pk=second)
                Wallet.objects.filter(pk=first).update(coins=models.F("coins") - 5)
                Wallet.objects.filter(pk=second).update(coins=models.F("coins") + 5)
            return "done"
        except OperationalError as e:
            return "deadlock" if "deadlock" in str(e).lower() else "error: " + str(e)[:80]
    return job


unordered = together(trade(a.pk, b.pk, False), trade(b.pk, a.pk, False))
ordered = together(trade(a.pk, b.pk, True), trade(b.pk, a.pk, True))
report(sorted(unordered) == ["deadlock", "done"] and ordered == ["done", "done"],
       f"Django {version} on Postgres: Ada paying Bo while Bo pays Ada, each locking their own wallet first, ended {sorted(unordered)}; "
       f"with both wallets locked in one query ordered by id, {ordered}")
