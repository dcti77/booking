from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy


class User(AbstractUser):
    photo = models.ImageField(upload_to="", verbose_name=gettext_lazy("Photo"), blank=True)
    country = models.CharField(max_length=200, verbose_name=gettext_lazy('Country'))
    town = models.CharField(max_length=200, verbose_name=gettext_lazy('Town'))
    phone = models.CharField(max_length=100, unique=True, verbose_name=gettext_lazy('Phone'))
    card = models.DecimalField(max_digits=16, decimal_places=0, verbose_name=gettext_lazy('Card'), null=True)
    valid_thru = models.DateField(verbose_name=gettext_lazy('Valid date'), null=True)

    SEX_CHOICE = [("male", "male"), ("female", "female")]

    sex = models.CharField(max_length=7, choices=SEX_CHOICE, default="male",
                           verbose_name=gettext_lazy('Sex'))

    LANG_CHOICE = [("en", "en"), ("ru", "ru")]

    language = models.CharField(max_length=3, choices=LANG_CHOICE, default='en',
                                verbose_name=gettext_lazy('Language'))  # middleware to make

    CURR_CHOICE = [("usd", "usd"), ("eur", "eur")]

    currency = models.CharField(max_length=3, choices=CURR_CHOICE, default='usd',
                                verbose_name=gettext_lazy('Currency'))


class Currency(models.Model):
    usd_to_eur = models.DecimalField(decimal_places=2, max_digits=2, max_length=10, default=1.20,
                                     verbose_name=gettext_lazy('euro/usd'))


class EmailSender(models.Model):
    subject = models.CharField(max_length=250, verbose_name=gettext_lazy('Subject'), null=True)
    adresses = models.CharField(max_length=2000, verbose_name=gettext_lazy('Adresses to send'))
    text = models.TextField(max_length=2000, verbose_name=gettext_lazy('Text'))

