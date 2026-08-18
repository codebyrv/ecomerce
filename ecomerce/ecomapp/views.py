from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html') 


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')    

    def post(self, request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if User.objects.filter(email=email).exists():
            messages.warning(request, "Email already exists")
            return render(request, 'register.html')

        if password != password2:
            messages.warning(request, "Passwords do not match")
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.warning(request, "Username already exists")
            return render(request, 'register.html')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html') 

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, "Invalid username or password, check again.")
            return render(request, 'login.html')    


class DashboardView(View):
    def get(self, request):
        messages.success(request, "welcome")
        return render(request, 'dashboard.html')