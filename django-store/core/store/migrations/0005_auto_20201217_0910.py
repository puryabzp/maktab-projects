# Generated by Django 3.1.2 on 2020-12-17 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0005_auto_20201217_0910'),
        ('store', '0004_auto_20201215_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_off',
        ),
        migrations.RemoveField(
            model_name='product',
            name='number_in_stock',
        ),
        migrations.RemoveField(
            model_name='product',
            name='off_percent',
        ),
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.ImageField(default='', upload_to='brand/images', verbose_name='image'),
        ),
        migrations.AddField(
            model_name='cart',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='product/images', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='productsimage',
            name='image',
            field=models.ImageField(default='', upload_to='products/images'),
        ),
        migrations.CreateModel(
            name='ShopProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_in_stock', models.IntegerField(verbose_name='number_in_stock')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', related_query_name='products', to='store.product', verbose_name='product')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', related_query_name='products', to='account.shop', verbose_name='shop')),
            ],
            options={
                'verbose_name': 'shop_product',
                'verbose_name_plural': 'shop_products',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ProductMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('label', models.CharField(max_length=150, verbose_name='brand_name')),
                ('property', models.TextField(verbose_name='property')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', related_query_name='product', to='store.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'product_meta',
                'verbose_name_plural': 'products_meta',
                'ordering': ['-created_at'],
            },
        ),
    ]
