# Generated by Django 5.0 on 2024-04-26 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userbookings_hotelname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbookings',
            name='Hotelname',
        ),
    ]
