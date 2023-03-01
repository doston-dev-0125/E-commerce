from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class Sub_Category(models.Model):
    name=models.CharField(max_length=150)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
    def __str__(self):
       return self.name

class Brand(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
      
class Product(models.Model):
    name=models.CharField(max_length=100)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    image=models.ImageField(upload_to='ecommerce/image')
    date=models.DateTimeField(auto_now_add=True)
    price=models.DecimalField(max_digits = 10, decimal_places = 2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=False,default='')
    sub_category=models.ForeignKey(Sub_Category,on_delete=models.CASCADE,null=False,default='')
    
    def __str__(self):
       return self.name
class Order(models.Model):
    image=models.ImageField(upload_to='ecommerce/order/image')
    product=models.CharField(max_length=1000,default='')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    quantity=models.CharField(max_length=5)
    price=models.DecimalField(max_digits = 10, decimal_places = 2)
    address=models.TextField()
    phone=models.CharField(max_length=14)
    pincode=models.CharField(max_length=15)
    total=models.CharField(max_length=1000,default='')
    date=models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.product