from django.shortcuts import render, redirect, get_object_or_404
from .forms import HotelSearchForm, HotelReservationForm
from hotels.models import Hotel


def reservation_home(request):
    if request.method == 'POST':
        form = HotelSearchForm(request.POST)
        if form.is_valid():
            return redirect(f'/reservation/search?country={form.cleaned_data["country"]}')
    else:
        form = HotelSearchForm()
    return render(request, 'reservation/booking_hotel.html', {'form': form})


def search(request):
    selection = Hotel.objects.filter(country=request.GET['country'])
    return render(request, 'reservation/selection.html', {'selection': selection})


def booking(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    if request.method == 'POST':
        form = HotelReservationForm(request.POST)
        if form.is_valid():
            return redirect('basket')
    else:
        form = HotelReservationForm()
    return render(request, 'reservation/booking.html', {'hotel': hotel, 'form': form})


def basket(request):
    return render(request, 'reservation/basket.html')
