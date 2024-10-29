from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'bought_price', 'market_price_today', 'expiry_date', 'is_low_stock', 'is_expiring_soon')
    # list_filter = ('is_low_stock', 'is_expiring_soon')
