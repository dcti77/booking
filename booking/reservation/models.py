from django.db import models

# Create your models here.
class Reservation(models.Model):
    country = models.CharField(max_length=250)
    hotel = models.CharField(max_length=250)
    number_of_person = models.IntegerField()
    number_of_nights = models.IntegerField()
    booking_date = models.DateField()
    rating = models.IntegerField()

