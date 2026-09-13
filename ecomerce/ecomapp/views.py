from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from ecomapp.models import*


class IndexView(View):

    def get(self, request):

        products = Product.objects.filter(
            category__is_active=True
        )

        return render(
            request,
            "index.html",
            {
                "products": products
            }
        )

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
         
            if product.stock > 0:
                cart[product_id_str] = 1
            else:
                messages.error(request, "Product is out of stock.")
                return redirect("product_detail", product_id=product.id)
                
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
    
    
    
# views.py

from django.shortcuts import render, redirect, get_object_or_404

from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages

from django.db import transaction

from .models import Product
from .models import Order
from .models import Orderitem
from .models import OrderTracking


# =========================================================
# CHECKOUT VIEW
# =========================================================

class CheckoutView(LoginRequiredMixin, View):

    # -----------------------------------------------------
    # GET METHOD
    # -----------------------------------------------------

    def get(self, request):

        # Get cart from session
        cart = request.session.get(
            "cart",
            {}
        )

        # List to store cart products
        cart_items = []

        # Total price
        total = 0


        # Loop through cart
        for product_id, quantity in cart.items():

            # Convert quantity to integer
            quantity = int(quantity)

            # Get product from database
            product = Product.objects.get(
                id=product_id
            )

            # Calculate product total
            item_total = (
                product.price * quantity
            )

            # Add product information
            cart_items.append({

                "product": product,

                "quantity": quantity,

                "item_total": item_total
            })

            # Add to total
            total = total + item_total


        # Send data to checkout.html
        return render(
            request,
            "checkout.html",
            {
                "cart_items": cart_items,

                "total": total
            }
        )


    # -----------------------------------------------------
    # POST METHOD
    # -----------------------------------------------------

    def post(self, request):

        # Get checkout details
        full_name = request.POST.get(
            "full_name"
        )

        email = request.POST.get(
            "email"
        )

        phone = request.POST.get(
            "phone"
        )

        address = request.POST.get(
            "address"
        )

        city = request.POST.get(
            "city"
        )

        state = request.POST.get(
            "state"
        )

        pincode = request.POST.get(
            "pincode"
        )


        # Get cart from session
        cart = request.session.get(
            "cart",
            {}
        )


        # -------------------------------------------------
        # CHECK EMPTY CART
        # -------------------------------------------------

        if not cart:

            # Show error message
            messages.error(
                request,
                "Your cart is empty."
            )

            # Return to cart
            return redirect("cart")


        # -------------------------------------------------
        # CHECK STOCK
        # -------------------------------------------------

        products = []

        total_amount = 0


        # Loop through cart
        for product_id, quantity in cart.items():

            # Convert quantity to integer
            quantity = int(quantity)

            # Get product
            product = get_object_or_404(
                Product,
                id=product_id
            )


            # Check stock
            if quantity > product.stock:

                # Show stock error
                messages.error(
                    request,
                    f"{product.product_name} has only "
                    f"{product.stock} items available."
                )

                # Don't create order
                return redirect("cart")


            # Store product and quantity
            products.append(
                (product, quantity)
            )


            # Calculate item total
            item_total = (
                product.price * quantity
            )

            # Add item total
            total_amount = (
                total_amount + item_total
            )


        # -------------------------------------------------
        # CREATE ORDER
        # -------------------------------------------------

        # Make database operation safe
        with transaction.atomic():

            # Create Order
            order = Order.objects.create(

                user=request.user,

                full_name=full_name,

                email=email,

                phone=phone,

                address=address,

                city=city,

                state=state,

                pincode=pincode,

                total_amount=total_amount,

                payment_status="Success",

                status="Order Placed"
            )


            # -------------------------------------------------
            # CREATE ORDER ITEMS
            # -------------------------------------------------

            for product, quantity in products:

                # Save purchased product
                Orderitem.objects.create(

                    order=order,

                    product=product,

                    quantity=quantity,

                    price=product.price
                )


                # -------------------------------------------------
                # REDUCE STOCK
                # -------------------------------------------------

                product.stock = (
                    product.stock - quantity
                )

                product.save(
                    update_fields=["stock"]
                )


            # -------------------------------------------------
            # CREATE FIRST TRACKING
            # -------------------------------------------------

            OrderTracking.objects.create(

                order=order,

                place="Order Processing",

                status="Order Placed"
            )


        # -------------------------------------------------
        # CLEAR CART
        # -------------------------------------------------

        request.session["cart"] = {}

        request.session.modified = True


        # -------------------------------------------------
        # REDIRECT TO SUCCESS PAGE
        # -------------------------------------------------

        return redirect(
            "order_success",
            order_id=order.id
        )


# =========================================================
# ORDER SUCCESS VIEW
# =========================================================

class OrderSuccessView(LoginRequiredMixin, View):

    def get(self, request, order_id):

        # Get user's order
        order = get_object_or_404(
            Order,
            id=order_id,
            user=request.user
        )

        # Show success page
        return render(
            request,
            "order_success.html",
            {
                "order": order
            }
        )


# =========================================================
# MY ORDERS VIEW
# =========================================================

class MyOrdersView(LoginRequiredMixin, View):

    def get(self, request):

        # Get current user's orders
        orders = Order.objects.filter(
            user=request.user
        ).order_by(
            "-created_at"
        )

        # Show orders
        return render(
            request,
            "my_orders.html",
            {
                "orders": orders
            }
        )


# # =========================================================
# # TRACK ORDER VIEW
# # =========================================================

# class TrackOrderView(LoginRequiredMixin, View):

#     def get(self, request, order_id):

#         # Get only current user's order
#         order = get_object_or_404(
#             Order,
#             id=order_id,
#             user=request.user
#         )


#         # Get tracking history
#         tracking = order.tracking.all().order_by(
#             "tracking_time"
#         )


#         # Show tracking page
#         return render(
#             request,
#             "track_order.html",
#             {
#                 "order": order,

#                 "tracking": tracking
#             }
#         )




# class TrackOrderView(LoginRequiredMixin, View):

#     def get(self, request, order_id):

#         order = get_object_or_404(
#             Order,
#             id=order_id,
#             user=request.user
#         )

#         tracking = OrderTracking.objects.filter(
#             order=order
#         ).order_by(
#             "tracking_time"
#         )

#         return render(
#             request,
#             "track_order.html",
#             {
#                 "order": order,
#                 "tracking": tracking
#             }
#         )


class TrackOrderView(LoginRequiredMixin, View):

    def get(self, request, order_id):

        # Get this user's order from the database
        order = get_object_or_404(
            Order,
            id=order_id,
            user=request.user
        )

        # Get tracking history from database
        tracking = order.tracking.all().order_by("tracking_time")

        return render(
            request,
            "track_order.html",
            {
                "order": order,
                "tracking": tracking
            }
        )