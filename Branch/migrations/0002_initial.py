# Generated by Django 4.0.1 on 2022-01-27 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Branch', '0001_initial'),
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch_product',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branch_product', to='Product.product', verbose_name='branch_product'),
        ),
    ]
