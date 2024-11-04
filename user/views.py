from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.template import RequestContext
from django.utils import timezone
from django.http import HttpResponse
from .models import User
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.hashers import check_password

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
                if check_password(password, user.password):
                    login(request, user)
                    user.last_login = timezone.now()
                    user.save()
                    return redirect('home')
                else:
                    form.add_error('password', 'Invalid password')
            except User.DoesNotExist:
                form.add_error('username', 'User not found')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


def handler404(request, exception=None):
    return render(request, '404.html', status=404)

def handler500(request, exception=None):
    return render(request, '500.html', status=404)

