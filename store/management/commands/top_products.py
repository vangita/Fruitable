from django.core.management.base import BaseCommand
from django.db.models import Count
from store.models import Product
from order.models import CartItem

class Command(BaseCommand):
    help = "Displays the top 3 most popular products based on user carts."

    def handle(self, *args, **kwargs):
        popular_products = (
            CartItem.objects
            .values('product')
            .annotate(user_count=Count('cart__user', distinct=True))
            .order_by('-user_count')[:3]
        )
        top_products = Product.objects.filter(id__in=[item['product'] for item in popular_products])

        self.stdout.write("Top 3 most popular products:")
        for item in popular_products:
            product = top_products.get(id=item['product'])
            self.stdout.write(f"{product.name}: {item['user_count']} users")
