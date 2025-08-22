from django.urls import path
from django.shortcuts import render
from .views import views_login , views_logout
app_name = 'accounts'

urlpatterns = [
    path('login', views_login , name='login'),
    path('logout/', views_logout , name='logout'),
]
