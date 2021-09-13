# Generated by Django 3.2 on 2021-07-02 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='currency',
            field=models.CharField(choices=[('usd', 'usd'), ('eur', 'eur')], default='usd', max_length=3, verbose_name='Currency'),
        ),
    ]
