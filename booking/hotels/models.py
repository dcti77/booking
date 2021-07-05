from django.db import models
from users.models import User, Currency


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    beds = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=2, default=0)
    rank = models.IntegerField()

    def price_to_eur(self):
        curr = User.objects.filter(id=request.user.id).currency
        if curr == 'eur':
            price_eur = self.price * Currency.usd_to_eur + 'eur'
            return price_eur
