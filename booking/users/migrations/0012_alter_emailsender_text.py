# Generated by Django 3.2 on 2021-07-03 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_emailsender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailsender',
            name='text',
            field=models.TextField(max_length=2000, verbose_name='Text'),
        ),
    ]
