# Generated by Django 3.1.2 on 2020-12-17 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20201217_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='', upload_to='category/images', verbose_name='image'),
        ),
    ]
