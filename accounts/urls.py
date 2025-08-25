from django.urls import path
from django.shortcuts import render
from .views import views_login , views_logout , views_signup , change_password
app_name = 'accounts'

urlpatterns = [
    path('login', views_login , name='login'),
    path('signup', views_signup , name='signup'),
    path('logout/', views_logout , name='logout'),
    path('change-password', change_password , name='change_password'),
]
