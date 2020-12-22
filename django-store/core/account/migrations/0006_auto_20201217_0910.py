# Generated by Django 3.1.2 on 2020-12-17 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20201217_0910'),
        ('account', '0005_auto_20201217_0910'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AddField(
            model_name='shop',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', related_query_name='shops', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_addresses', related_query_name='user_addresses', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
