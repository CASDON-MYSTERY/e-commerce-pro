# Generated by Django 3.1.5 on 2022-02-15 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0006_auto_20220207_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, null=True, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, default='0', max_length=150, null=True, verbose_name='size'),
        ),
        migrations.AlterField(
            model_name='size',
            name='description',
            field=models.CharField(max_length=150, verbose_name='description'),
        ),
    ]
