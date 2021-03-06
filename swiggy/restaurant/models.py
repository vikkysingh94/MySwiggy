from django.db import models
from s_admin.models import Areamodel,RestaurantTypeModel
from django.urls import reverse




class RestaurantModel(models.Model):
    restro_id = models.AutoField(primary_key=True)
    restro_name = models.CharField(unique=True,max_length=30)
    restro_contact = models.IntegerField(unique=True)
    restro_email = models.EmailField(max_length=100,unique=True)
    restro_area = models.ForeignKey(Areamodel,on_delete=models.CASCADE)
    restro_type = models.ForeignKey(RestaurantTypeModel,on_delete=models.CASCADE)
    restro_password = models.CharField(max_length=30)
    restro_otp = models.IntegerField()
    restro_status = models.CharField(max_length=30,default=False)
    def __str__(self):
        return self.restro_name

class RestaurantProduct(models.Model):
    product_id=models.AutoField(primary_key=True)
    restro_name=models.CharField(max_length=60)
    product_name=models.CharField(max_length=60,unique=True)
    product_quantity=models.IntegerField()
    product_price=models.FloatField()
    product_discount=models.FloatField()
    product_status=models.CharField(max_length=500)
    product_result=models.FloatField(null='True')
    Product_image=models.FileField(upload_to='Restro/', null='True',blank='True')
    Product_img=models.ImageField(upload_to='Restaurant/', default='Restaurant/food6.jpg', null='True',blank='True')

    def __str__(self):
        return self.product_id