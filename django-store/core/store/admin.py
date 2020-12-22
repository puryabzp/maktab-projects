from django.contrib import admin
from .models import *
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(ProductsImage)
admin.site.register(Cart)
admin.site.register(Shop)
admin.site.register(ShopProduct)
admin.site.register(ProductMeta)

# Register your models here.
