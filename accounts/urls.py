from django.urls import path
from django.shortcuts import render
from .views import views_login , views_logout , views_signup
app_name = 'accounts'

urlpatterns = [
    path('login', views_login , name='login'),
    path('signup', views_signup , name='signup'),
    path('logout/', views_logout , name='logout'),
]
