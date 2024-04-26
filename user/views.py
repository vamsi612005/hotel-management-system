from django.shortcuts import render, redirect
from hotel.models import hoteldetails
from django.core.mail import send_mail
import razorpay
from .models import userbookings
from django.contrib.auth.models import User


# Create your views here.
def test(request):
    return render(request,'usert/test.html')


def userviewhotel(request):
    hotels = hoteldetails.objects.all()
    return render(request, 'usert/userviewhotel.html', {'hotels': hotels})


def userhome(request):
    return render(request, 'usert/userhome.html')


def userviewprofile(request):
    return render(request, 'usert/userviewprofile.html',)


def useraddemail(request):
    if request.method == "POST":
        email = request.POST.get('emailu')
        cuser = request.user
        cuser.email=email
        cuser.save()
        return render(request,'usert/userviewprofile.html')


def useraddfirstname(request):
    if request.method == "POST":
        email = request.POST.get('firstnameu')
        cuser = request.user
        print(cuser.email)
        cuser.first_name=email
        cuser.save()
        return render(request,'usert/userviewprofile.html')


def useraddlastname(request):
    if request.method == "POST":
        email = request.POST.get('lastnameu')
        cuser = request.user
        print(cuser.email)
        cuser.last_name=email
        cuser.save()
        return render(request,'usert/userviewprofile.html')


def bookaroom(request,pk):
    print(pk)
    hotel = hoteldetails.objects.get(id=pk)
    return render(request, 'usert/bookaroom.html', {'hotel':hotel})


def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        recipient_email = '2200031906cseh@gmail.com'
        subject = 'This feedback is from ' + name + ' bearing the email id ' + email
        message_body = message
        send_mail(
            subject,
            message_body,
            '2200031906cseh@gmail.com',
            [recipient_email],
            fail_silently=False,
        )
        return render(request,'usert/contactus.html')
    else:
        return render(request,'usert/contactus.html')


def standardbooking(request,pk,value):
    return render(request,'usert/userStandardBooking.html', {'pk':pk,'value':value})


def bookingsuccess(request):
    return render(request,'usert/bookingsuccess.html')


def bookingdatasave(request,pk,value):
    if request.method == "POST":
        checkin=request.POST.get('Check_in')
        checkout=request.POST.get('Check_out')
        adults=request.POST.get('adults')
        children=request.POST.get('children')
        Name=request.POST.get('Name')
        Surname=request.POST.get('Surname')
        Email=request.POST.get('Email')
        Phone_Number=request.POST.get('Phone_Number')
        City=request.POST.get('City')
        Country=request.POST.get('Country')
        Address=request.POST.get('Address')
        data = userbookings(checkin=checkin,
                            checkout=checkout,
                            adults=adults,
                            children=children,
                            Name=Name,
                            Surname=Surname,
                            Email=Email,
                            Phone_Number=Phone_Number,
                            City=City,
                            Country=Country,
                            Address=Address)
        data.save()
        hotel=hoteldetails.objects.get(id=pk)
        hotelname=hotel.hotelname
        return render(request, 'usert/confirmbooking.html',{"hotelname": hotelname, "data": data, "value":value})
    return render(request, 'usert/userStandardBooking.html')


def confirmbooking(request):
    if request.method == "POST":
        amount = 50000
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_akJqYFF93KjSKX','i7mAQxA7PTDkK56I5B04mhkW'))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture':'1'})
        return render(request,'usert/success.html')
    return render(request,'usert/confirmbooking.html')
