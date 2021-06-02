from django.urls import path
from . import views


urlpatterns = [
    path('', views.reservation_home, name='reservation_home'),
    path('search/', views.search, name='search'),
    path('basket/<int:basket_id>/', views.show_basket, name='basket'),
]
