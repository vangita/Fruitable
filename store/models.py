from django.db import models

# Create your models here.
from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    description = models.TextField(max_length=500, verbose_name=_('description'))
    slug = models.SlugField(max_length=100, unique=True, verbose_name=_('slug'))
    parent = models.ForeignKey('self',  on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    description = models.TextField(max_length=500, verbose_name=_('description'))
    slug = models.SlugField(max_length=100, unique=True,verbose_name=_('slug'))
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=True, related_name='products', verbose_name=_('tag'))
    image = VersatileImageField(upload_to='products/', null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    is_in_stock = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.name