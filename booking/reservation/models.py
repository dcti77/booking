from django.db import models

from hotels.models import Hotel
from users.models import User


class Reservation(models.Model):
    number_of_person = models.PositiveIntegerField()
    number_of_nights = models.PositiveIntegerField()
    booking_date = models.DateField()

    def __str__(self):
        return self.country, self.hotel


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return "Basket"
