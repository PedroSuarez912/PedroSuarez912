from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=25)
    edad = models.IntegerField()
    altura = models.FloatField()
    matrimonio = models.BooleanField()
    nacimiento = models.DateField()
