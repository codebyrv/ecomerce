from django.contrib import admin
from django.urls import path,include


from ecomapp.views import*

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('login', Logout.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('dashboard',DashboardView.as_view(), name='dashboard'),
    
]