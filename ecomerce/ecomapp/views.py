from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from ecomapp.models import*


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



class Logout(View):
    
    def get(self,request):
        
        logout(request)
        messages.success(request, "LOGOUT success")
        return render ('home')
   


class DashboardView( LoginRequiredMixin, View):
    def get(self, request):
        products=Product.objects.all()
        messages.success(request, "welcome")
        return render(request, 'dashboard.html',{'products':products})
    
    
class ProductDetailView(LoginRequiredMixin, View):    
    def get(self, request, product_id):
        
        product=Product.objects.get(id=product_id)
        
        return render(request,'productdetail.html',{'product':product})
    
    
    
    
class CartView(LoginRequiredMixin,View):
    
    def get(self,request):
        
        
            cart=request.session.get('cart',{})
            
            
            products=[] 
            
            total=0
            
            
            for product_id,quantity in cart.items():
                
                
                product=get_object_or_404(Product,id=product_id) 
                
                
                
                subtotal=product.price * quantity         
                
                
                total=total+subtotal
                
                products.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal
            })
                
                
            return render(request,'cart.html',{'products':products,'total':total})
        
        
        
class AddToCartView(LoginRequiredMixin,View):
    
    def get(self,request,product_id):
        
        cart=request.session.get('cart',{})
        
        product=get_object_or_404(Product,id=product_id)
        
        
        
        product_id_str=str(product_id)
        
        if product_id in cart:
            
            if cart[product_id]<product.stock:
                
                cart[product_id]+=1
        else:
            cart[product_id]=1
            if cart[product_id]>product.stock:
                
                cart[product_id]= 1
                
        request.session['cart']=cart
        
        request.session.modified=True
        
        
        return redirect('cart')
    
    
    
class IncreaseCartView(LoginRequiredMixin, View):

    def get(self, request, product_id):

        product = get_object_or_404(Product, id=product_id)

        cart = request.session.get('cart', {})

        product_id = str(product.id)

        if product_id in cart:

            if cart[product_id] < product.stock:

                cart[product_id] += 1

        request.session['cart'] = cart

        request.session.modified = True

        return redirect('cart')


class DecreaseCartView(LoginRequiredMixin, View):

    def get(self, request, product_id):

        cart = request.session.get('cart', {})

        product_id = str(product_id)

        if product_id in cart:

            if cart[product_id] > 1:

                cart[product_id] -= 1

            else:

                del cart[product_id]

        request.session['cart'] = cart

        request.session.modified = True

        return redirect('cart')
    
    
    
class CheckoutView(LoginRequiredMixin,View):
    
    def get(self,request):
        
        cart=request.session.get('cart',{})
        
        cart_items=[]
        
        total=0 
        
        for product_id,quantity in cart.items():
            
            product=Product.objects.get(id=product_id)
            
            
            item_total=product.price*quantity
            
            cart_items.append({
                
                'product':product,
                'quantity':quantity,
                'item_total':item_total
                
            })    
            
            
            total=total+item_total
            
            return render(request,'checkout.html',{
                
                
                'cart_items':cart_items,
                'total':total
                
            })