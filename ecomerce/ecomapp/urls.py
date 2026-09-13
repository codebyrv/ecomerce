from django.contrib import admin
from django.urls import path, include

from ecomapp.views import *

urlpatterns = [

    path('', IndexView.as_view(), name='home'),

    path('login/', LoginView.as_view(), name='login'),

    path('logout/', Logout.as_view(), name='logout'),

    path('register/', RegisterView.as_view(), name='register'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path(
        'product/<int:product_id>/',
        ProductDetailView.as_view(),
        name='product_detail'
    ),

    path(
        'cart/',
        CartView.as_view(),
        name='cart'
    ),

    path(
        'add-to-cart/<int:product_id>/',
        AddToCartView.as_view(),
        name='add_to_cart'
    ),

    path(
        'cart/increase/<int:product_id>/',
        IncreaseCartView.as_view(),
        name='increase_cart'
    ),

    path(
        'cart/decrease/<int:product_id>/',
        DecreaseCartView.as_view(),
        name='decrease_cart'
    ),
    
     path(
        'checkout',
        CheckoutView.as_view(),
        name='checkout'
    ),
     
     path(
        "order-success/<int:order_id>/",
        OrderSuccessView.as_view(),
        name="order_success"
    ),


    # User's orders
    path(
        "my-orders/",
        MyOrdersView.as_view(),
        name="my_orders"
    ),


    # Track particular order
    path(
        "track-order/<int:order_id>/",
        TrackOrderView.as_view(),
        name="track_order"
    ),
]