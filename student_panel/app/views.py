from django.shortcuts import render,redirect
from app.models import *
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages


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

def index(request):
    return render(request,"index.html")

def index_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        if User.objects.filter(email=email).exists():
            obj = User.objects.get(email=email)
            variable_password = obj.password
            if check_password(password,variable_password):
                return redirect("/dashboard/")
            else:
                messages.error(request,"Password Incorrect")
                return redirect("/index/")
        else:
            messages.error(request,"Email is not registered")
            return redirect("/index/")
        
def courses(request):
    return render(request,"courses.html")




def dashboard(request):
    return render(request,"dashboard.html")



def viewstudents(request):
    return render(request,"viewstudents.html")



