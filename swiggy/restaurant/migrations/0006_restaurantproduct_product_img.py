# Generated by Django 3.0.5 on 2020-05-08 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_restaurantproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantproduct',
            name='Product_img',
            field=models.ImageField(blank='True', null='True', upload_to='Restaurant/'),
            preserve_default='True',
        ),
    ]
