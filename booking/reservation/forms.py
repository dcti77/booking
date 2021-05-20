from django import forms


class HotelSearch(forms.Form):
    country = forms.CharField(max_length=200)
    name = forms.CharField(max_length=200, required=False)
    number_of_person = forms.IntegerField()
    number_of_nights = forms.IntegerField()
    booking_date = forms.DateField()
    rank = forms.IntegerField()
