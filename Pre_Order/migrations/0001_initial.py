# Generated by Django 4.0.1 on 2022-01-27 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pre_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(blank=True, default=0, verbose_name='qty')),
            ],
            options={
                'verbose_name': 'Pre_Order',
                'verbose_name_plural': 'Pre_Orders',
            },
        ),
    ]
