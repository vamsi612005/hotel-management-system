from django.shortcuts import render, redirect, get_object_or_404
from .forms import hoteldetailsform, hotelstaffmanagement
from .models import hoteldetails, staffmanagement
from user.models import userbookings
from django.contrib.auth.models import User

# Create your views here.
def hotelhome(request):
    return render(request,'hotelt/hotelhome.html')


def uploadhotel(request):
    if request.method == 'POST':
        form = hoteldetailsform(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('viewhotel')
    else:
        form = hoteldetailsform()

    return render(request, 'hotelt/uploadhotel.html', {'form': form})


def viewhotel(request):
    hotels = hoteldetails.objects.all()
    return render(request, 'hotelt/viewhotel.html',{'hotels': hotels})


def hotelviewprofile(request):
    return render(request, 'hotelt/hotelviewprofile.html',)


def hoteladdemail(request):
    if request.method == "POST":
        email = request.POST.get('emailu')
        cuser = request.user
        cuser.email=email
        cuser.save()
        return render(request,'hotelt/hotelviewprofile.html')


def hoteladdfirstname(request):
    if request.method == "POST":
        email = request.POST.get('firstnameu')
        cuser = request.user
        print(cuser.email)
        cuser.first_name=email
        cuser.save()
        return render(request,'hotelt/hotelviewprofile.html')


def hoteladdlastname(request):
    if request.method == "POST":
        email = request.POST.get('lastnameu')
        cuser = request.user
        print(cuser.email)
        cuser.last_name=email
        cuser.save()
        return render(request,'hotelt/hotelviewprofile.html')


def hotelstaffmanagementht(request):
    staff = staffmanagement.objects.all()
    return render(request, 'hotelt/hotelstaffmanagement.html',{'staff': staff})


def hoteladdstaff(request):
    if request.method == 'POST':
        form = hotelstaffmanagement(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('hotelstaffmanagementht')
    else:
        form = hotelstaffmanagement()
    return render(request, 'hotelt/hoteladdstaff.html', {'form': form})


def deletehotel(request):
    if request.method == 'POST':
        obj_id = request.POST.get('obj_id')
        obj = get_object_or_404(hoteldetails, id=obj_id)
        obj.delete()
        return redirect('viewhotel')  # Redirect to your list view after deletion
    return redirect('viewhotel')


def updatehotel(request, obj_id):
    obj = get_object_or_404(hoteldetails, id=obj_id)
    if request.method == 'POST':
        form = hoteldetailsform(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('viewhotel')  # Redirect to your list view after updating
    else:
        form = hoteldetailsform(instance=obj)
    return render(request, 'hotelt/updatehotel.html', {'form': form})


def deletestaff(request):
    if request.method == 'POST':
        obj_id = request.POST.get('obj_id')
        obj = get_object_or_404(staffmanagement, id=obj_id)
        obj.delete()
        return redirect('hotelstaffmanagementht')  # Redirect to your list view after deletion
    return redirect('hotelstaffmanagementht')


def updatestaff(request, obj_id):
    obj = get_object_or_404(staffmanagement, id=obj_id)
    if request.method == 'POST':
        form = hotelstaffmanagement(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('hotelstaffmanagementht')  # Redirect to your list view after updating
    else:
        form = hoteldetailsform(instance=obj)
    return render(request, 'hotelt/updatestaff.html', {'form': form})


def hotelroombooking(request):
    bookings = userbookings.objects.all()
    return render(request,'hotelt/hotelroombookings.html',{"bookings": bookings})
