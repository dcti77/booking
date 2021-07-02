from django.test import TestCase
from datetime import date

from django.urls import reverse

from .forms import HotelReservationForm
from .models import Reservation
from hotels.models import Hotel
from users.models import User


class BasketViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', password='password')
        self.hotel = Hotel.objects.create(
            name='Hotel',
            country='Country',
            town='Town',
            beds=40,
            rank=4
        )
        self.reservation = Reservation.objects.create(
            user=self.user,
            hotel=self.hotel,
            number_of_person=2,
            number_of_nights=10,
            booking_date=date(2021, 8, 10)
        )

    def test_html_basket(self):
        response = self.client.get('/reservation/basket/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_template_basket(self):
        response = self.client.get('/reservation/basket/', follow=True)
        self.assertTemplateUsed(response, 'reservation/basket.html')

    def test_base(self):
        self.assertEqual(Reservation.objects.count(), 1)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('basket'))
        self.assertEqual(response.status_code, 200)


class HotelReservationFormTest(TestCase):
    def test_past_date(self):
        data = date(2018, 12, 1)
        form_data = {'booking_date': data}
        form = HotelReservationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_card_valid(self):
        data = date(2018, 12, 1)
        form_data = {'valid_thru': data}
        form = HotelReservationForm(data=form_data)
        self.assertFalse(form.is_valid())
