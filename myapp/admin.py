from django.contrib import admin
from .models import Item, Order, OrderItem

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']

admin.site.register(Item, ItemAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
