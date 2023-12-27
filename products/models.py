from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length = 50) 

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length = 25)
    discount = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f'{self.name} {self.discount}%'


class Product(models.Model):
    name = models.CharField(max_length = 50)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE, related_name = 'products')
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'products')
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Color(models.Model):
    name = models.CharField(max_length = 25)

    def __str__(self) -> str:
        return self.name


class Size(models.Model):
    name = models.CharField(max_length = 25)

    def __str__(self) -> str:
        return self.name


class ProductVersion(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = 'version')
    image = models.ImageField(upload_to='product', null=True, blank=True)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    color = models.ForeignKey(Color, on_delete = models.CASCADE, related_name = 'product_color')
    size = models.ForeignKey(Size, on_delete = models.CASCADE, related_name = 'product_size')
    discount = models.ForeignKey(Discount, on_delete = models.CASCADE, null = True, blank = True, related_name = 'product_discount')
    display = models.BooleanField(default = False)

    def __str__(self) -> str:
        return f'{self.product.name} {self.color.name} {self.size.name}'
    

class ProductImages(models.Model):
    image = models.ImageField(upload_to='products')
    product = models.ForeignKey(ProductVersion, on_delete = models.CASCADE, related_name = 'images')

    def __str__(self) -> str:
        return f'{self.product.product.name} {self.product.color.name} {self.product.size.name}'


class ProductsComment(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = 'comments')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'comment')
    rating = models.SmallIntegerField()
    comment = models.TextField()
    date = models.DateField(auto_now_add = True)

    def __str__(self) -> str:
        return f'{self.product.name} {self.user.full_name} {self.rating}'


class Commentimages(models.Model):
    comment = models.ForeignKey(ProductsComment, on_delete = models.CASCADE, related_name = 'comment_images')
    image = models.ImageField(upload_to='comments')