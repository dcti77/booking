from django.shortcuts import render, redirect
from .forms import HotelSearch
from hotels.models import Hotel
from django.utils.translation import gettext as _


def reservation_home(request):
    if request.method == 'POST':
        form = HotelSearch(request.POST)
        if form.is_valid():
            return redirect(f'/reservation/search?country={form.cleaned_data["country"]}')
    else:
        form = HotelSearch()
    return render(request, 'reservation/booking_hotel.html', {'form': form})


def search(request):
    selection = _(Hotel.objects.filter(country=request.GET['country']))
    return render(request, 'reservation/selection.html', {'selection': selection})
