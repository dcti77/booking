from django import forms
from django.utils.translation import gettext_lazy


class HotelSearchForm(forms.Form):
    country = forms.CharField(max_length=200, label=gettext_lazy('Country'))
    name = forms.CharField(max_length=200, required=False, label=gettext_lazy('Name'))
    number_of_person = forms.IntegerField(label=gettext_lazy('Number_of_person'))
    number_of_nights = forms.IntegerField(label=gettext_lazy('Number_of_nights'))
    booking_date = forms.DateField(label=gettext_lazy('Booking_date'))
    rank = forms.IntegerField(label=gettext_lazy('Rank'))


class HotelReservationForm(forms.Form):
    number_of_person = forms.IntegerField(label=gettext_lazy('Number_of_person'))
    number_of_nights = forms.IntegerField(label=gettext_lazy('Number_of_nights'))
    booking_date = forms.DateField(label=gettext_lazy('Booking_date'))
    card = forms.DecimalField(max_digits=16, decimal_places=0, label=gettext_lazy('Card'))
    valid_thru = forms.DateField(label=gettext_lazy('Valid_thru'))
