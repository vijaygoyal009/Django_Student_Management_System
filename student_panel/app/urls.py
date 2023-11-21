from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path("",views.sign_up),
    path("registration/",views.registration),
    path("index/",views.index),
    path("index_login/",views.index_login),
    path("courses/",views.courses),
    path("dashboard/",views.dashboard),
    path("viewstudents/",views.viewstudents),    
]