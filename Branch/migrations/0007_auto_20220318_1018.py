# Generated by Django 3.1.5 on 2022-03-18 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Branch', '0006_auto_20220313_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multiple_size',
            name='branch_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='multiple_size_branch_product', to='Branch.branch_product', verbose_name='multiple_size_branch_product'),
        ),
    ]