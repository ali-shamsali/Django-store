from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages

# Create your views here.

def views_login(request):
    if request.user.is_authenticated:
        return redirect('root:home') 
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('root:home')  
        else:
            messages.error(request, "نام کاربری یا رمز عبور اشتباه است")
    return render(request,'accounts/login.html')

def views_logout(request):
    logout(request)
    return redirect('accounts:login')
