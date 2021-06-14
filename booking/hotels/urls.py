from django.urls import path
from . import views
from .views import SearchResultsView, HomePageView


urlpatterns = [
    path('', views.hotel, name='hotel'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('home/', HomePageView.as_view(), name='home'),
]
