from django.contrib import admin

from store.models import Category, Product, Tag


# Register your models here.



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity', 'description')
    list_filter = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'parent')
    list_filter = ('name',)
    fields = ('name', 'description', 'slug', 'parent', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'parent':
            kwargs["queryset"] = Category.objects.filter(is_active=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin,)