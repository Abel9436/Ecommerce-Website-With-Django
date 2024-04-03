from django.db import models

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=50)
    product_description=models.TextField()
    product_price=models.DecimalField(max_digits=5,decimal_places=2)
    product_rating=models.IntegerField()
    product_image1=models.ImageField()
    product_image2=models.ImageField()
    catagory_id=models.ForeignKey('Catagory',on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
    
class User(models.Model):
    product_id=models.IntegerField(primary_key=True)
    FUll_name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=10)
    adresss=models.CharField(max_length=50)
    role=models.CharField(choices=[('Buyer','Buyer'),('Seller','Seller')],max_length=50,default='Buyer')

class Catagory(models.Model):
    catagoty_id=models.IntegerField(primary_key=True)   
    catagory_name=models.CharField(max_length=50)
class Cart(models.Model):
    product_id=models.ForeignKey('Product',on_delete=models.CASCADE)
    user_id=models.ForeignKey('User',on_delete=models.CASCADE)
    quantity=models.IntegerField()
    cart_id=models.IntegerField(primary_key=True)
class Order(models.Model):
    product_id=models.ForeignKey('Product',on_delete=models.CASCADE)
    user_id=models.ForeignKey('User',on_delete=models.CASCADE)
    quantity=models.IntegerField()
    order_id=models.IntegerField(primary_key=True)
    orger_status=models.CharField(choices=[('Pending','Pending'),('Shipped','Shipped'),('Delivered','Delivered')],default='Pending',max_length=50)
class Payment(models.Model):
    payment_id=models.IntegerField(primary_key=True)
    order_id=models.ForeignKey('Order',on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=5,decimal_places=2)
    payment_id=models.IntegerField(primary_key=True) 
    payment_method=models.CharField(choices=[('Cash On Delivery','Cash On Delivery'),('Online','Online')],default='Cash On Delivery',max_length=50)
    payment_status=models.CharField(choices=[('Pending','Pending'),('Successfull','Successfull'),('Failed','Failed')],default='Pending',max_length=50)