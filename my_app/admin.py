from django.contrib import admin
from .models import Menu, Comment, Order, OrderItem

admin.site.register(Menu)
admin.site.register(Comment)
admin.site.register(Order)
admin.site.register(OrderItem)
# Register your models here.
