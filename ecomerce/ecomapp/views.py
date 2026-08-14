from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User

from django.contrib import messages
 
# Create your views here.


class IndexView(View):
    
    def get(self,request):
        
        return render (request,'index.html') 
    


class LoginView(View):
    
    def get(self,request):
        
        return render (request,'login.html') 
    
  
    
    
class RegisterView(View):
    
    def get(self,request):
    
        return render (request,'register.html')    
    
    
    def post(self,request):
        username=request.POST.get("username")
        name=request.POST.get("name")
        email=request.POST.get("email")
       
        password=request.POST.get("password")
        password2=request.POST.get("password2")
        
        if User.objects.filter(email=email).exists():
            
            messages.warning("email already exists")
            
            
        elif password != password2:
            
            messages.warning(request,"password not matching")  
            
            
        elif User.objects.filter(username=username).exists(): 
            
            messages.warning("username already exists")
            
            
        else:
            
            User.objects.create_user(username=username,name=name,email=email,password=password)   
            
            
        return redirect('')