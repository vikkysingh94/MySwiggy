# Generated by Django 3.0.5 on 2020-04-18 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_delete_restaurantmodel'),
        ('s_admin', '0003_restautanttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantTypeModel',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='RestautantType',
        ),
    ]
