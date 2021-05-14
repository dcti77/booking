from django.shortcuts import render
from hotels.models import Hotel


def hotel(request):
    if request.method == 'GET':
        return render(request, 'hotels.html', {'hotels': Hotel.objects.all()})
