from django.contrib import admin

from order.models import UserCart, CartItem

admin.site.register(UserCart)
admin.site.register(CartItem)
