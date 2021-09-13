from django.db import models

from hotels.models import Hotel
from users.models import User


class Reservation(models.Model):
    number_of_person = models.PositiveIntegerField()
    number_of_nights = models.PositiveIntegerField()
    booking_date = models.DateField() # в форме работает как charfield, не предлагает выбора даты
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)
    card = models.DecimalField(max_digits=16, decimal_places=0, null=True)  # в модели users/User есть такое же поле
    valid_thru = models.DateField(null=True)  # в модели users/User есть такое же поле
    finish = models.BooleanField(null=True)

    def __str__(self):
        return "Booking"
