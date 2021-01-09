from django.contrib import admin
from .models import ContactMessages


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name' , 'date_added']




admin.site.register(ContactMessages, ContactAdmin)
