from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'discount', 'added_on']
    list_filter = ['category', 'added_on']
    search_fields = ['name', 'category__name']
    list_editable = ['price', 'discount']  # Allow editing these fields directly in the list view

admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'date_time', 'transaction_id']
    list_filter = ['date_time']
    search_fields = ['user__username', 'transaction_id']
    date_hierarchy = 'date_time'  # Provides a hierarchy navigation by date

admin.site.register(Order, OrderAdmin)

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', 'discount', 'final_price']
    list_filter = ['order']
    search_fields = ['order__id', 'product__name']

admin.site.register(OrderProduct, OrderProductAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    search_fields = ['user__username']

admin.site.register(Cart, CartAdmin)

class CartProductAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity']
    list_filter = ['cart']
    search_fields = ['cart__id', 'product__name']
    # This ensures that the product-cart combination is unique within the admin interface
    def get_unique_for_model(self, model):
        if model == CartProduct:
            return ('product', 'cart')
        return super().get_unique_for_model(model)

admin.site.register(CartProduct, CartProductAdmin)