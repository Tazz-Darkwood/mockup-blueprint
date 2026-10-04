"""A timer kept as a timestamp and worked out when someone looks needs no clock running on the server."""
import datetime
from _setup import report, setup, tables
version = setup()
from django.db import models
from django.utils import timezone


class Egg(models.Model):
    laid_at = models.DateTimeField()
    HATCH_AFTER = datetime.timedelta(hours=6)

    class Meta:
        app_label = "game"

    def state(self, now):
        return "hatched" if now >= self.laid_at + self.HATCH_AFTER else "incubating"


tables(Egg)
now = timezone.now()
egg = Egg.objects.create(laid_at=now - datetime.timedelta(hours=5))
before, after = egg.state(now), egg.state(now + datetime.timedelta(hours=2))
ready = Egg.objects.filter(laid_at__lte=now + datetime.timedelta(hours=2) - Egg.HATCH_AFTER).count()
report(timezone.is_aware(now) and before == "incubating" and after == "hatched" and ready == 1,
       f"Django {version}: timezone.now() carries its time zone: {timezone.is_aware(now)}. An egg laid five hours ago is {before} now and {after} two hours later, "
       f"worked out from laid_at alone; one query for 'ready to hatch by then' found {ready}")
