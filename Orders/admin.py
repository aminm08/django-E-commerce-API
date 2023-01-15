from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ( 'product', 'quantity', 'price', )
    show_change_link = True
    ordering = ['-quantity']
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number',  'user', 'is_paid', 'datetime_created', )
    search_fields = ('first_name', 'last_name', 'phone_number', )
    list_filter = ('is_paid', )
    inlines = [
        OrderItemInline,
    ]

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('cover_preview','order', 'product', 'quantity', 'price', )
    search_fields = ('price', )
    ordering = ('-price', )



admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)