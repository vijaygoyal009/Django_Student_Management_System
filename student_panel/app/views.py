from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password


# Create your views here.
def sign_up(request):
    return render(request,"sign-up.html")

def registration(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        if User.objects.filter(email = email).exists():
            return HttpResponse("Email Already registered !")
        else:
            User.objects.create(name=name, email = email, password=password)
            return HttpResponse("Stdent Sign Up Successfully!")


def courses(request):
    return render(request,"courses.html")

def dashboard(request):
    return render(request,"dashboard.html")

def index(request):
    return render(request,"index.html")


def viewstudents(request):
    return render(request,"viewstudents.html")



