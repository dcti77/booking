from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from hotels.models import Hotel


def reservation_home(request):
    if request.method == 'POST':
        form = HotelSearch(request.POST)
        if form.is_valid():
            return redirect(f'/reservation/search?country={form.cleaned_data["country"]}')
    else:
        form = HotelSearch()
    return render(request, 'reservation/booking_hotel.html', {'form': form})


def search(request):
    selection = Hotel.objects.filter(country=request.GET['country'])
    return render(request, 'reservation/selection.html', {'selection': selection})


def show_basket(request, basket_id):
    basket = get_object_or_404(Hotel, pk=basket_id)
    form = HotelReservation(request.POST)

    context = {
        'post': basket,
        'title': 'Basket',
        'form': form
    }

    return render(request, 'reservation/basket.html', context=context)
