from django.db import models
from category.models import Category

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=5)
   
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

        
    
class ProductDetail(models.Model):
    description=models.TextField()
    brand=models.CharField(max_length=100)
    stock=models.IntegerField(default=0)
    product=models.OneToOneField(Product,on_delete=models.CASCADE,related_name='details')

    def __str__(self):
        return self.brand







   