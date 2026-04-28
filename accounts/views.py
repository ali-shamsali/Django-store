from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
User = get_user_model()


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=False) 
    image = forms.ImageField(required=False)

    class Meta:
        model = User 
        fields = ('id_code', 'email', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'input-password', 'placeholder': 'رمز عبور'})
        self.fields['password2'].widget.attrs.update({'class': 'input-password', 'placeholder': 'تأیید رمز عبور'})
        self.fields['id_code'].widget.attrs.update({'class': 'input-email-account', 'maxlength': '10', 'pattern': '[0-9]{10}', 'title': 'کد ملی باید ۱۰ رقم باشد'})
        self.fields['email'].widget.attrs.update({'class': 'input-email-account'})
        self.fields['image'].widget.attrs.update({'accept': 'image/*'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.id_code = self.cleaned_data['id_code']
        user.email = self.cleaned_data['email']
        user.image = self.cleaned_data['image']
        if commit:
            user.save()
        return user

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
            messages.error(request, "کد ملی یا رمز عبور اشتباه است")
    return render(request, 'accounts/login.html')

def views_signup(request):
    if request.user.is_authenticated:
        return redirect('root:home')

    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)  
        if form.is_valid():
            user = form.save() 
            login(request, user)
            messages.success(request, "ثبت‌نام با موفقیت انجام شد 🎉")
            return redirect('root:home')
        else:
            messages.error(request, "خطایی در ثبت‌نام وجود دارد")
    else:
        form = SignupForm()  
    return render(request, 'accounts/signup.html', {'form': form})

def views_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('accounts:login')

def change_password(request):
    return render(request,'accounts/password-change.html')