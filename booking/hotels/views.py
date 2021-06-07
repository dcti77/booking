from django.shortcuts import render
from hotels.models import Hotel
from django.views.generic.list import ListView


def hotel(request):
    if request.method == 'GET':
        print(Hotel.objects.all())
        return render(request, 'hotels/hotels.html', {'hotels': Hotel.objects.all()})


class HotelView(ListView):
    model = Hotel
    template_name = 'hotels.html'
    context_object_name = 'hotel'


class SearchResultsView(ListView):
    model = Hotel
    template_name = 'hotels/search_results.html'
    queryset = Hotel.objects.filter(country__icontains='United States')
