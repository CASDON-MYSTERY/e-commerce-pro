# Generated by Django 3.1.5 on 2022-05-05 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Credit_Sales', '0007_credit_sale_expected_amount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='credit_sale',
            options={'ordering': ['-date'], 'verbose_name': 'Credit_Sale', 'verbose_name_plural': 'Credit_Sales'},
        ),
    ]