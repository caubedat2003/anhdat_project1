# Generated by Django 3.1.12 on 2025-03-04 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20250304_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='customer_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product_id',
            field=models.CharField(max_length=24),
        ),
    ]
