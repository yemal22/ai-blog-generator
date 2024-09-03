from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import signupForm, loginForm
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json

# Create your views here.
def signup_user(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already exists')
                elif User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    messages.success(request, 'User created successfully')
                    return redirect('login-user')
            else:
                messages.error(request, 'Passwords do not match')
        else:
            messages.error(request, 'Invalid form')
    else:
        form = signupForm()
    return render(request, 'blog_generator/signup.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid form')
    else:
        form = loginForm()
    return render(request, 'blog_generator/login.html', {'form': form})
        
def logout_user(request):
    logout(request)
    return redirect('login-user')

@login_required(login_url='login-user')
def index(request):
    return render(request, 'blog_generator/index.html')

@csrf_exempt
def generate_blog(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            yt_link = data['link']

        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error': 'Invalid Request method'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid Request method'}, status=405)