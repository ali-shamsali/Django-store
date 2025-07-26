from django.urls import path
from django.shortcuts import render
from .views import home , contact , about

urlpatterns = [
    path('', home),
    path('contact', contact),
    path('about', about),
]
