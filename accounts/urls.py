from django.urls import path
from django.shortcuts import render
from .views import views_login
app_name = 'accounts'

urlpatterns = [
    path('login', views_login , name='login'),
]
