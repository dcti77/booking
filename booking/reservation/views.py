from django.shortcuts import render
from .forms import HotelSearch
from hotels.models import Hotel


def reservation_home(request):
    if request.method == 'POST':
        form = HotelSearch(request.POST)
        if form.is_valid():
            selection = Hotel.objects.filter(country=form.cleaned_data['country'])
            return render(request, 'reservation/selection.html', {'selection': selection})
    else:
        form = HotelSearch()
    return render(request, 'reservation/booking_hotel.html', {'form': form})
