from django.urls import path
from . import views


urlpatterns = [
    path('', views.reservation_home, name='reservation_home'),
    path('search/', views.search, name='search'),
    path('booking/<int:hotel_id>/', views.booking, name='booking'),
    path('basket/', views.basket, name='basket'),
]
