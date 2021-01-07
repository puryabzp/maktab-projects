from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("category_name", "slug")
    list_display = ("category_name", 'created_at', 'slug', "parent")
    list_filter = ("category_name", "slug")
    prepopulated_fields = {"slug": ("category_name",), }
    date_hierarchy = "created_at"


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    search_fields = ("brand_name", "slug")
    list_display = ("brand_name", 'created_at', 'updated_at', 'slug')
    list_filter = ("brand_name", "slug")
    prepopulated_fields = {"slug": ("brand_name",), }
    date_hierarchy = "created_at"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("title", "slug")
    list_display = ("title", 'description', 'created_at', 'updated_at', 'slug')
    list_filter = ("title", "slug")
    prepopulated_fields = {"slug": ("title",), }
    date_hierarchy = "created_at"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ("brand_name", "slug")
    list_display = ("product", 'content', 'author')
    list_filter = ("author", "product")
    date_hierarchy = "created_at"


@admin.register(ShopProduct)
class ShopProductAdmin(admin.ModelAdmin):
    search_fields = ("shop", "product")
    list_display = ("shop", 'product', 'number_in_stock')
    list_filter = ("shop", "product")
    date_hierarchy = "created_at"


@admin.register(ProductMeta)
class ProductMetaAdmin(admin.ModelAdmin):
    search_fields = ("product", "label")
    list_display = ("product", 'label', "property")
    list_filter = ("product", "label")
    date_hierarchy = "created_at"


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    search_fields = ("user", "name")
    list_display = ("user", 'name', "description")
    list_filter = ("user", "name")
    date_hierarchy = "created_at"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", 'description')


@admin.register(OrderItems)
class OrderItemAdmin(admin.ModelAdmin):
    list_filter = ("order", "shop_product")
    list_display = ("order", 'shop_product', 'count', 'price')
    search_fields = ("order", "shop_product")


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", 'product', 'condition')


@admin.register(BasketItems)
class BasketItemAdmin(admin.ModelAdmin):
    list_display = ("basket", 'product')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("order", 'user', 'amount')


admin.site.register(ProductsImage)
admin.site.register(Basket)

# Register your models here.
