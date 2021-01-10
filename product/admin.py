from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name' , 'price']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product' , 'order' , 'quantity' , 'date_added']
    list_filter = ('order',)

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['order', 'customer','city' , 'state' , 'zipcode' , 'address' , 'email']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer' , 'complete']
    list_filter = ('complete',)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name' , 'email']

admin.site.register(Customer , CustomerAdmin)
admin.site.register(Product , ProductAdmin)
admin.site.register(Order , OrderAdmin)
admin.site.register(OrderItem , OrderItemAdmin)
admin.site.register(ShippingAdress , ShippingAddressAdmin)
admin.site.register(Category , CategoryAdmin)


# Register your models here.

