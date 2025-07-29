from django.urls import path
from django.shortcuts import render
from .views import home , contact , about

app_name = 'root'

urlpatterns = [
    path('', home , name='home'),
    path('contact', contact , name='contact'),
    path('about', about , name='about'),
]
