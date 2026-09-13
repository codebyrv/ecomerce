from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import (
    Order,
    Category,
    Product,
    Orderitem,
    OrderTracking
)


@admin.register(Category)
class CategoryAdmin(ModelAdmin):

    list_display = (
        "id",
        "name",
        "is_active",
    )


@admin.register(Product)
class ProductAdmin(ModelAdmin):

    list_display = (
        "id",
        "product_name",
        "category",
        "price",
        "stock",
    )


@admin.register(Order)
class OrderAdmin(ModelAdmin):

    list_display = (
        "id",
        "user",
        "full_name",
        "total_amount",
        "payment_status",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "payment_status",
    )


@admin.register(Orderitem)
class OrderItemAdmin(ModelAdmin):

    list_display = (
        "order",
        "product",
        "quantity",
        "price",
    )


@admin.register(OrderTracking)
class OrderTrackingAdmin(ModelAdmin):

    list_display = (
        "order",
        "place",
        "status",
        "tracking_time",
    )

    list_filter = (
        "status",
    )