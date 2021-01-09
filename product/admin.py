from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name' , 'price']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product' , 'order' , 'quantity' , 'date_added']

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['order', 'customer']

admin.site.register(Customer)
admin.site.register(Product , ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem , OrderItemAdmin)
admin.site.register(ShippingAdress , ShippingAddressAdmin)
admin.site.register(Category)


# Register your models here.

