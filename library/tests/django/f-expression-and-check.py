"""An update written with F() is safe without a lock, and a CHECK constraint refuses a balance below zero."""
from _setup import report, setup, tables, together
version = setup("postgres")
from django.db import IntegrityError, models


class Wallet(models.Model):
    coins = models.IntegerField()

    class Meta:
        app_label = "game"
        constraints = [models.CheckConstraint(condition=models.Q(coins__gte=0), name="coins_never_negative")]


tables(Wallet)
wallet = Wallet.objects.create(coins=100)
spend = lambda: Wallet.objects.filter(pk=wallet.pk).update(coins=models.F("coins") - 10)
together(spend, spend)
after_two = Wallet.objects.get(pk=wallet.pk).coins
try:
    Wallet.objects.filter(pk=wallet.pk).update(coins=models.F("coins") - 500)
    refused = "nothing: the overdraft was allowed"
except IntegrityError as e:
    refused = "IntegrityError naming " + ("coins_never_negative" if "coins_never_negative" in str(e) else "no constraint")
left = Wallet.objects.get(pk=wallet.pk).coins
report(after_two == 80 and "coins_never_negative" in refused and left == 80,
       f"Django {version} on Postgres: two purchases at the same moment written as update(coins=F('coins') - 10) left {after_two} of 100; "
       f"spending 500 raised {refused} and left {left}")
