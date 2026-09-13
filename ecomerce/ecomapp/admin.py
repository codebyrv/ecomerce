from django.contrib import admin


from .models import*
# Register your models here.


admin.site.register(Category)
admin.site.register(Product)


# admin.py

from django.contrib import admin

from .models import Order
from .models import Orderitem
from .models import OrderTracking


# =========================================================
# ORDER ADMIN
# =========================================================

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    # Columns shown in admin
    list_display = (
        "id",
        "user",
        "full_name",
        "total_amount",
        "payment_status",
        "status",
        "created_at",
    )

    # Filters on right side
    list_filter = (
        "status",
        "payment_status",
    )


# =========================================================
# ORDER ITEM ADMIN
# =========================================================

@admin.register(Orderitem)
class OrderItemAdmin(admin.ModelAdmin):

    # Display purchased products
    list_display = (
        "order",
        "product",
        "quantity",
        "price",
    )


# =========================================================
# ORDER TRACKING ADMIN
# =========================================================

@admin.register(OrderTracking)
class OrderTrackingAdmin(admin.ModelAdmin):

    # Display tracking information
    list_display = (
        "order",
        "place",
        "status",
        "tracking_time",
    )

    # Filter by status
    list_filter = (
        "status",
    )