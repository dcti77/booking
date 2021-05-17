from django import forms
from .models import *


class HotelSearch(forms.Form):
    country = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    number_of_person = models.PositiveIntegerField()
    umber_of_nights = models.PositiveIntegerField()
    booking_date = models.DateField()
    rank = models.IntegerField()
