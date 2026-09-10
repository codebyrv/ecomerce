from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Category(models.Model):
    
    name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    
    product_name=models.CharField(max_length=100)
    
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.CharField(max_length=100)
    
    price=models.PositiveIntegerField()
    image=models.ImageField(upload_to='product_images')    
    stock = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.product_name
    
    
    
class Order(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    full_name=models.CharField(max_length=100)
    
    email=models.EmailField()
    
    phone=models.CharField(max_length=100)
    
    city=models.CharField( max_length=100)
    
    state=models.CharField(max_length=100)
    
    pincode=models.CharField(max_length=100)
    
    
    total_amount=models.PositiveBigIntegerField()
    
    
    payment_status=models.CharField(max_length=50,default="success")    
    
    status=models.CharField(max_length=50,default="order places") 
    
    
    created_at=models.DateTimeField(auto_now_add=True) 
    
    
    def __str__(self):
        return f"Order#{self.id}-{self.user.username}"
      