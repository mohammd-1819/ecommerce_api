from django.contrib import admin
from . import models


class CartItemAdmin(admin.TabularInline):
    model = models.CartItem


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)
    inlines = (CartItemAdmin,)


class OrderItemAdmin(admin.TabularInline):
    model = models.OrderItem


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_paid')
    inlines = (OrderItemAdmin,)
    list_filter = ('is_paid',)
