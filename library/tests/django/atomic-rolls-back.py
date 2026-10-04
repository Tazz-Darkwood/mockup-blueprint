"""Inside transaction.atomic, an error undoes every write made in the block."""
from _setup import report, setup, tables
version = setup("postgres")
from django.db import models, transaction


class Wallet(models.Model):
    owner = models.CharField(max_length=20)
    coins = models.IntegerField()

    class Meta:
        app_label = "game"


tables(Wallet)
Wallet.objects.create(owner="ada", coins=100)
Wallet.objects.create(owner="bo", coins=0)


def pay(inside_atomic):
    def move():
        Wallet.objects.filter(owner="ada").update(coins=models.F("coins") - 30)
        raise RuntimeError("the server fell over between the two halves of the payment")
    try:
        if inside_atomic:
            with transaction.atomic():
                move()
        else:
            move()
    except RuntimeError:
        pass
    return Wallet.objects.get(owner="ada").coins


plain = pay(False)
Wallet.objects.filter(owner="ada").update(coins=100)
atomic = pay(True)
report(plain == 70 and atomic == 100,
       f"Django {version} on Postgres: a payment that failed halfway left Ada with {plain} of 100 coins and Bo with nothing more (30 coins gone); "
       f"the same failure inside transaction.atomic left her with {atomic}")
