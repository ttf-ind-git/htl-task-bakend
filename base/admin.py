from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
# admin.site.register(Customer)

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ('username',)
    list_display = ['username', 'email', 'first_name', 'last_name', 'latitude', 'longitude']
    list_filter = ['username', 'email', 'first_name']
    
admin.site.register(Customer, CustomerAdmin)