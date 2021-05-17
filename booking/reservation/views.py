from django.shortcuts import render
from .forms import HotelSearch


def reservation_home(request):
    form = HotelSearch()
    return render(request, 'reservation/booking_hotel.html', {'form': form})
