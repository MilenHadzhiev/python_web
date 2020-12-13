from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=25, blank=False)
