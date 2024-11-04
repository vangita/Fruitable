from order.models import UserCart
from store.models import Category, Tag



def global_context(request):
    item_count = 0
    if request.user.is_authenticated:
            user_cart = UserCart.objects.get(user=request.user)
            item_count = sum(item.quantity for item in user_cart.items.all())
    context = {
        'par_categories': Category.objects.filter(parent__isnull=True),
        'tags' : Tag.objects.all(),
        'user' : request.user,
        'item_count': item_count,
    }
    return context
