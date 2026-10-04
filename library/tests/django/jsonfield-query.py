"""A JSONField on Postgres keeps structured data such as a genome and can be searched by what is inside it."""
from _setup import report, setup, tables
version = setup("postgres")
from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=20)
    genome = models.JSONField()

    class Meta:
        app_label = "game"


tables(Pet)
Pet.objects.create(name="Mud", genome={"version": 1, "body": ["A1", "a2"], "glow": True})
Pet.objects.create(name="Pearl", genome={"version": 1, "body": ["a2", "a2"], "glow": False})
glowing = list(Pet.objects.filter(genome__glow=True).values_list("name", flat=True))
carriers = list(Pet.objects.filter(genome__body__contains="A1").values_list("name", flat=True))
back = Pet.objects.get(name="Pearl").genome
report(glowing == ["Mud"] and carriers == ["Mud"] and back["body"] == ["a2", "a2"],
       f"Django {version} on Postgres: filter(genome__glow=True) found {glowing}; filter(genome__body__contains='A1') found {carriers}; a genome read back as {back}")
