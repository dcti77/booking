from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from datetime import date


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

    def clean_renewal_date(self):
        data = self.cleaned_data['booking_date']
        if data < date.today():
            raise ValidationError(gettext_lazy('Invalid date - renewal in past'))
        return data

    def clean_card_valid(self):
        data = self.cleaned_data['valid_thru']
        if data < date.today():
            raise ValidationError(gettext_lazy('Invalid date - renewal in past'))
        return data
