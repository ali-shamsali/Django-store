from django.shortcuts import render

# Create your views here.

def views_login(request):
    return render(request,'accounts/login.html')
