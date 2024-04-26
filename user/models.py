from django.db import models
from django.contrib.auth.models import User


class userbookings(models.Model):
    checkin = models.DateField()
    checkout = models.DateField()
    adults = models.IntegerField()
    children = models.IntegerField()
    Name = models.CharField(max_length=255)
    Surname = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Phone_Number = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    Address = models.TextField()

