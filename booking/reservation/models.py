from django.db import models


class Reservation(models.Model):
    number_of_person = models.PositiveIntegerField()
    number_of_nights = models.PositiveIntegerField()
    booking_date = models.DateField()

    def __str__(self):
        return self.country, self.hotel
