from django.test import TestCase
from hotels.models import Hotel


class CheckPages(TestCase):

    def test_hotels_page_status_code(self):
        response = self.client.get('/hotels/')
        self.assertEqual(response.status_code, 200)

    def test_hotels_search_page_status_code(self):
        response = self.client.get('/hotels/search/?q=test')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['object_list'], [])


class HotelTestCase(TestCase):

    def setUp(self):
        self.hotel1 = Hotel.objects.create(name='Baccarat', country='United States', town='NY', beds='3', rank='9')
        self.hotel2 = Hotel.objects.create(name='Bacca', country='United States', town='NY', beds='3', rank='9')

    def test_hotels(self):
        response = self.client.get('/hotels/search/?q=Bacc')
        self.assertQuerysetEqual(response.context['object_list'], [self.hotel1, self.hotel2], ordered=False)
