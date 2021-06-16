from django.shortcuts import render, redirect, get_object_or_404

from .forms import HotelSearchForm, HotelReservationForm
from hotels.models import Hotel
from .models import Reservation


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
            Reservation.objects.create(
                number_of_person=form.cleaned_data['number_of_person'],
                number_of_nights=form.cleaned_data['number_of_nights'],
                booking_date=form.cleaned_data['booking_date'],
                user=request.user,
                hotel=Hotel.objects.get(pk=hotel_id),
                card=form.cleaned_data['card'],
                valid_thru=form.cleaned_data['valid_thru'],
            )
            return redirect('/reservation/basket/')
    else:
        form = HotelReservationForm()
    return render(request, 'reservation/booking.html', {'hotel': hotel, 'form': form})


def basket(request):
    form = Reservation.objects.all()
    context = {
        'form': form
    }
    return render(request, 'reservation/basket.html', context=context)


def delete_hotel(request, pk):
    if request.method == 'POST':
        hotel = Reservation.objects.get(pk=pk)
        hotel.delete()
    return redirect('/reservation/basket/')
