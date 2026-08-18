from django.db import models

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
    
    def __str__(self):
        return self.product_name