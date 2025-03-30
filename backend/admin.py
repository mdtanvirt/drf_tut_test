from django.contrib import admin
from .models import Product, Order, OrderItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'image')
    search_fields = ('name', 'price')

# Alternative way to register in admin without using decorator
#admin.site.register(Product, ProductAdmin)

admin.site.register(Order)
admin.site.register(OrderItem)