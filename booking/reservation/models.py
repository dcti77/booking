from django.db import models


class Reservation(models.Model):
    country = models.CharField(max_length=250)
    hotel = models.CharField(max_length=250)
    number_of_person = models.IntegerField()
    number_of_nights = models.IntegerField()
    booking_date = models.DateField()
    rating = models.IntegerField()

    def __str__(self):
        return self.country, self.hotel


class User(models.Model):
    first_name = models.CharField(max_length=80)
    middle_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    phone = models.CharField(max_length=100, unique=True)
    card = models.DateField(max_digits=16, decimal_places=0)
    valid_thru = models.DateField()
