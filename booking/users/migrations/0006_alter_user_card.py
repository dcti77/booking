# Generated by Django 3.2 on 2021-06-21 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210616_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='card',
            field=models.DecimalField(decimal_places=0, max_digits=16, null=True, verbose_name='Card'),
        ),
    ]