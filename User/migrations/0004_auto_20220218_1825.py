# Generated by Django 3.1.5 on 2022-02-18 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20220218_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='full_name',
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_name',
            field=models.CharField(default='not set', max_length=255, verbose_name='customer_name'),
            preserve_default=False,
        ),
    ]
