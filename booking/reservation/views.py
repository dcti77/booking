from django.shortcuts import render


def index(request):
    return render(request, 'reservation/booking_hotel.html')
