# Generated by Django 3.0.5 on 2020-05-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_auto_20200524_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantproduct',
            name='product_result',
            field=models.FloatField(null='True'),
        ),
    ]
