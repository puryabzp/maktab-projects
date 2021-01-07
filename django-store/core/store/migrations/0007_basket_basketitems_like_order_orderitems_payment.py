# Generated by Django 3.1.2 on 2020-12-31 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0006_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='basket', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'basket',
                'verbose_name_plural': 'baskets',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('description', models.TextField(verbose_name='description')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='amount')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='items', related_query_name='items', to='store.order', verbose_name='order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', related_query_name='payment', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'payment',
                'verbose_name_plural': 'payments',
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='count')),
                ('price', models.IntegerField(verbose_name='price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', related_query_name='order_items', to='store.order', verbose_name='order')),
                ('shop_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', related_query_name='products', to='store.shopproduct', verbose_name='shop_product')),
            ],
            options={
                'verbose_name': 'Order_item',
                'verbose_name_plural': 'order_items',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', related_query_name='like', to='store.product', verbose_name='Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', related_query_name='like', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'like',
                'verbose_name_plural': 'likes',
            },
        ),
        migrations.CreateModel(
            name='BasketItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket_item', to='store.basket', verbose_name='basket')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket_item', to='store.shopproduct', verbose_name='item')),
            ],
            options={
                'verbose_name': 'basket_item',
                'verbose_name_plural': 'basket_items',
            },
        ),
    ]