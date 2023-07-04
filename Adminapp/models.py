from django.db import models

# Create your models here.
class Products(models.Model):
    product_name=models.CharField(max_length=40)
    product_type=models.CharField(max_length=40)
    product_desc=models.TextField(max_length=40)
    product_category=models.CharField(max_length=40)
    product_price=models.IntegerField(default=0)
    product_image=models.ImageField(upload_to='images',default='null.jpg')
    def __str__(self):
        return self.product_name

