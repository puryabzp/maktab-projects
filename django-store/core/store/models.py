from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from account.models import *

User = get_user_model()


class Category(models.Model):
    category_name = models.CharField(_('category_name'), max_length=150)
    image = models.ImageField(_('image'), upload_to='category/images', default='')
    slug = models.SlugField(_('slug'), unique=True, db_index=True)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated_at'))
    parent = models.ForeignKey('self', verbose_name=_('Parent'), related_name='children', related_query_name='children',
                               null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")
        ordering = ['-created_at']

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    brand_name = models.CharField(_('brand_name'), max_length=150)
    slug = models.SlugField(_('slug'), unique=True, db_index=True)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated_at'))
    image = models.ImageField(_('image'), upload_to='brand/images',default='')

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")
        ordering = ['-created_at']

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    title = models.CharField(_('title'), max_length=150, db_index=True)
    description = models.TextField(_('description'))
    slug = models.SlugField(_('slug'), unique=True, db_index=True)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated_at'))
    category = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.SET_NULL,
                                 related_name='products',
                                 null=True, blank=True)
    brand = models.ForeignKey(Brand, verbose_name=_('brand'), related_name='products', related_query_name='products',
                              on_delete=models.CASCADE)
    product_properties = models.TextField(_('product_properties'))
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=100)
    is_available = models.BooleanField(_('is_available'), default=True)
    product_scores = models.IntegerField(_('product_scores'), default=0)
    image = models.ImageField(_('image'), upload_to='product/images',default='')

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class ProductsImage(models.Model):
    name = models.CharField(_('name'), max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images',default='')

    class Meta:
        verbose_name = _("image_product")
        verbose_name_plural = _("image_products")
        ordering = ['-name']

    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.TextField(_("Content"))
    product = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE, related_name='comments',
                                related_query_name='comments')
    created_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Update at"), auto_now=True)
    author = models.ForeignKey(User, verbose_name=_("Author"), on_delete=models.SET_NULL, null=True, blank=True)
    is_confirmed = models.BooleanField(_("confirm"), default=True)

    class Meta:
        verbose_name = _("comment")
        verbose_name_plural = _("comments")
        ordering = ['-created_at']

    def __str__(self):
        return self.content


class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name=_('user'), null=True, blank=True, on_delete=models.CASCADE)
    slug = models.SlugField(_('slug'), unique=True, null=True, blank=True)
    created_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Update at"), auto_now=True)
    products = models.ManyToManyField(Product, verbose_name=_('products'), blank=True, default=None)
    subtotal = models.DecimalField(_('subtotal'), default=0.00, decimal_places=2, max_digits=100)
    total = models.DecimalField(_('total'), default=0.00, decimal_places=2, max_digits=100)
    count = models.PositiveIntegerField(_('count'), default=0)

    class Meta:
        verbose_name = _("cart")
        verbose_name_plural = _("carts")
        ordering = ['-created_at']

    def __str__(self):
        return self.user


class ShopProduct(models.Model):
    shop = models.ForeignKey(Shop, verbose_name='shop', related_name='products', related_query_name='products',
                             on_delete=models.CASCADE)
    number_in_stock = models.IntegerField(_('number_in_stock'))
    product = models.ForeignKey(Product, verbose_name='product', related_name='products', related_query_name='products',
                                on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Update at"), auto_now=True)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=100)

    class Meta:
        verbose_name = _("shop_product")
        verbose_name_plural = _("shop_products")
        ordering = ['-created_at']

    def __str__(self):
        return self.shop.name


# Create your models here.
class ProductMeta(models.Model):
    product = models.ForeignKey(Product, verbose_name='product', related_name='product', related_query_name='product',
                                on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Update at"), auto_now=True)
    label = models.CharField(_('brand_name'), max_length=150)
    property = models.TextField(_('property'))

    class Meta:
        verbose_name = _("product_meta")
        verbose_name_plural = _("products_meta")
        ordering = ['-created_at']

    def __str__(self):
        return self.label

