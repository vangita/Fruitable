from django.urls import path
from .views import  CartView, CartAddItemView

app_name = 'order_app'

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CartView.as_view() , name='checkout'),
    path('cart/add/<int:product_id>/', CartAddItemView.as_view(), name='add_to_cart')
]