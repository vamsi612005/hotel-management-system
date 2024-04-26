from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def signinup(request):
    return render(request,'authentication/signinup.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Usename already taken')
                return render(request, 'authentication/signinup.html')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.info(request, 'Account created successfully!!')
                if username != "hotel":
                    return render(request, 'usert/userhome.html')
                else:
                    return render(request, 'hotelt/hotelhome.html')
        else:
            messages.info(request, 'Password do not match')
            return render(request, 'authentication/signinup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=username, password=pass1)
        if user is not None:
            auth.login(request, user)
            if len(username)<5:
                return render(request, 'usert/userhome.html')
            else:
                return render(request, 'hotelt/hotelhome.html')
        else:
            messages.info(request, 'Invalid username or password.')
            return render(request, 'authentication/signinup.html')
    else:
        return render(request, 'authentication/signinup.html')


def logout(request):
    auth.logout(request)
    return redirect('signinup')