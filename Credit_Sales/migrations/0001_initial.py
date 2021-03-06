# Generated by Django 4.0.1 on 2022-01-27 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credit_Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='total_amount')),
                ('remark', models.CharField(max_length=200, verbose_name='remark')),
                ('date', models.DateField(auto_now_add=True, verbose_name='date')),
            ],
            options={
                'verbose_name': 'Credit_Sale',
                'verbose_name_plural': 'Credit_Sales',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='amount')),
                ('date', models.DateField(auto_now_add=True, verbose_name='date')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
    ]
