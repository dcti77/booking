from django import forms


class HotelSearch(forms.Form):
    country = forms.CharField(max_length=200, label="Страна")
    name = forms.CharField(max_length=200, label="Название гостиницы", required=False)
    number_of_person = forms.IntegerField(label="Количество человек")
    number_of_nights = forms.IntegerField(label="Количество ночей")
    booking_date = forms.DateField(label="Дата бронирования")
    rank = forms.IntegerField(label="Рейтинг", required=False)
