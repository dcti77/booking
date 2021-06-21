from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy
from six import text_type


class User(AbstractUser):
    photo = models.ImageField(upload_to="", verbose_name=gettext_lazy("Photo"), blank=True)
    country = models.CharField(max_length=200, verbose_name=gettext_lazy('Country'))
    town = models.CharField(max_length=200, verbose_name=gettext_lazy('Town'))
    phone = models.CharField(max_length=100, unique=True, verbose_name=gettext_lazy('Phone'))
    card = models.DecimalField(max_digits=16, decimal_places=0, verbose_name=gettext_lazy('Card'), null=True)
    valid_thru = models.DateField(verbose_name=gettext_lazy('Valid date'), null=True)

    SEX_CHOICE = [("male", "male"), ("female", "female")]

    sex = models.CharField(max_length=7, choices=SEX_CHOICE, default="male", verbose_name=gettext_lazy('Sex'))

