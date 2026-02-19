from django.db import models
from category.models import Category

# Create your models here.


class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10,decimal_places=5)
    image_url=models.URLField(max_length=500)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name