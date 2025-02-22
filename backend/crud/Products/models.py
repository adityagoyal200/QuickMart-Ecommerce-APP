from django.db import models
from base.models import *

class Category(BaseModel):
    category_name = models.CharField(max_length=50)
    category_img = models.ImageField(upload_to ="categories")
    slug = models.SlugField(unique=True,null=True,blank=True)

    
class Product(BaseModel):
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    price = models.IntegerField()
    product_desc = models.TextField()
    slug = models.SlugField(unique=True,null=True,blank=True)
    
class ProductImage(BaseModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_images")    
    image = models.ImageField(upload_to="categories")
    slug = models.SlugField(unique=True,null=True,blank=True)