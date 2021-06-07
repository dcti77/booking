from django.urls import path
from . import views
from .views import SearchResultsView


urlpatterns = [
    path('', views.hotel, name='hotel'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]
