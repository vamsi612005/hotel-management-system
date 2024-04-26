from django.db import models


class hoteldetails(models.Model):
    hotelname = models.CharField(max_length=255)
    noofrooms = models.IntegerField()
    hoteldesc = models.TextField()
    hotellocation = models.CharField(max_length=255)
    hotelavgroomcostpn = models.IntegerField()
    hotelimage = models.ImageField(upload_to='static/media/hotelimages/', null=True, blank=True)
    standardprice = models.IntegerField(default=50)
    deluxeprice = models.IntegerField(default=100)
    suiteprice = models.IntegerField(default=150)


class staffmanagement(models.Model):
    empid=models.IntegerField()
    empname=models.CharField(max_length=255)
    branch=models.CharField(max_length=255)
    workingas=models.CharField(max_length=255)
    intimehr=models.IntegerField()
    intimemin=models.IntegerField()
    outtimehr=models.IntegerField()
    outtimemin=models.IntegerField()
    shiftno=models.IntegerField()
    paycheck=models.IntegerField()
