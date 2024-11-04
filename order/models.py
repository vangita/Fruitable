from django.db import models

from store.models import Product
from user.models import User


class UserCart(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      cart = models.ManyToManyField(Product, through='CartItem')

      def __str__(self):
            return f"Cart of {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(UserCart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in cart"

    @property
    def total_price(self):
        return self.quantity * self.product.price