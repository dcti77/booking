from django.shortcuts import render
from hotels.models import Hotel
# from django.views.generic.list import ListView
from django.views.generic import TemplateView, ListView
from django.db.models import Q


def hotel(request):
    if request.method == 'GET':
        print(Hotel.objects.all())
        return render(request, 'hotels/hotels.html', {'hotels': Hotel.objects.all()}) # hotels/hotels.html не нашел урла в hotels\urls.py


class HotelView(ListView):
    model = Hotel
    template_name = 'hotels.html'
    context_object_name = 'hotel'


class HomePageView(TemplateView):
    template_name = 'hotels/home.html'


# class SearchResultsView(ListView):
#     model = Hotel
#     template_name = 'hotels/search_results.html'
#     queryset = Hotel.objects.filter(country__icontains='United States')

class SearchResultsView(ListView):
    model = Hotel
    template_name = 'hotels/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Hotel.objects.filter(
            Q(name__icontains=query) | Q(country__icontains=query)
        )
        return object_list
