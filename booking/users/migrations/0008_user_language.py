# Generated by Django 3.2 on 2021-06-23 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_valid_thru'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('en', 'en'), ('ru', 'ru')], default='en', max_length=3, verbose_name='Language'),
        ),
    ]