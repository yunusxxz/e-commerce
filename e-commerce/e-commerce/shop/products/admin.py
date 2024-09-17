from django.contrib import admin

from .models import Product, Tag, ProductImage, Category, Brand

# Register your models here.
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Brand)