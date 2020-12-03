# Generated by Django 3.1.2 on 2020-11-13 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201113_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentlike',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_like', related_query_name='comment_like', to='blog.comment', verbose_name='Comment'),
        ),
    ]