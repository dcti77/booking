# Generated by Django 3.2 on 2021-05-05 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('town', models.CharField(max_length=200)),
                ('beds', models.IntegerField()),
                ('rank', models.IntegerField()),
            ],
        ),
    ]