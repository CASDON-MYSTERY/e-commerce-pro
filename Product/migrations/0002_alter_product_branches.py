# Generated by Django 3.2.11 on 2022-02-01 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Branch', '0003_alter_branch_product_branch_and_more'),
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='branches',
            field=models.ManyToManyField(blank=True, null=True, related_name='products_branches', to='Branch.Branch', verbose_name='branches'),
        ),
    ]
