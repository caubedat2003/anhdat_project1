# Generated by Django 3.1.12 on 2025-03-04 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20250304_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='customer_id',
            field=models.IntegerField(),
        ),
    ]
