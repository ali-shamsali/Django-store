from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

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

def views_signup(request):
    if request.user.is_authenticated:
        return redirect('root:home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()   
            login(request, user) 
            messages.success(request, "ثبت‌نام با موفقیت انجام شد 🎉")
            return redirect('root:home')
        else:
            messages.error(request, "خطایی در ثبت‌نام وجود دارد")
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def views_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('accounts:login')
