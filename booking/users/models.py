from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    country = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    phone = models.CharField(max_length=100, unique=True)
    card = models.DecimalField(max_digits=16, decimal_places=0, null=True)
    valid_thru = models.DateField(null=True)

    SEX_CHOICE = [("male", "male"), ("female", "female")]

    sex = models.CharField(max_length=7, choices=SEX_CHOICE, default="male")
