from django.shortcuts import render


def reservation_home(request):
    return render(request, 'reservation/booking_hotel.html')
