from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path("",views.sign_up),
    path("registration/",views.registration),
    path("courses/",views.courses),
    path("dashboard/",views.dashboard),
    path("index/",views.index),
    path("viewstudents/",views.viewstudents),    
]