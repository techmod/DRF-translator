from django.db import models

class Translator(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    result = models.FloatField()
