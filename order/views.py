from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, RedirectView

from store.models import Product
from order.models import UserCart, CartItem


# Create your views here.



class CheckoutView(TemplateView):
    template_name = 'checkout.html'


class CartView(TemplateView):
    template_name = 'cart.html'


class CartAddItemView(LoginRequiredMixin, RedirectView):
    def get_success_url(self):
        referer_url = self.request.META.get('HTTP_REFERER')

        return referer_url if referer_url else reverse('generic_category_listing')

    def get_redirect_url(self, *args, **kwargs):
        product_id = kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        cart, created = UserCart.objects.get_or_create(user=self.request.user)

        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not item_created:
            cart_item.quantity += 1
            cart_item.save()
        else:
            cart_item.quantity = 1
            cart_item.save()
        return self.get_success_url()