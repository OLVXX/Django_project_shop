from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("You are logged in.")
        else:
            return HttpResponse("Invalid login details.")
    else:
        return render(request, 'login.html')
