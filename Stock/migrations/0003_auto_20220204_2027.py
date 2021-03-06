# Generated by Django 3.1.5 on 2022-02-04 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0005_auto_20220204_1826'),
        ('Stock', '0002_auto_20220204_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='branch_product',
        ),
        migrations.AddField(
            model_name='stock',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='stock_product', to='Product.product', verbose_name='product'),
            preserve_default=False,
        ),
    ]
