from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    beds = models.IntegerField()
    # price = models.FloatField
    rank = models.IntegerField()
