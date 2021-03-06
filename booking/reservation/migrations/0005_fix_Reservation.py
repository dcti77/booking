# Generated by Django 3.2 on 2021-06-14 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservation', '0004_basket'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='finish',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotels.hotel'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Basket',
        ),
    ]
