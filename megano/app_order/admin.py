from django.contrib import admin

from app_order.models import Order, OrderStatus


class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'created', 'status']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)
