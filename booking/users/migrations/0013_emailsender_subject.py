# Generated by Django 3.2 on 2021-07-05 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_emailsender_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailsender',
            name='subject',
            field=models.CharField(max_length=250, null=True, verbose_name='Subject'),
        ),
    ]
