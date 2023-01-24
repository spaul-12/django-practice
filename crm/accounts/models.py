from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    data_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Tags(models.Model):
    tags = models.CharField(max_length=200,null=False)

    def __str__(self) -> str:
        return self.tags
 


class Product(models.Model):
    CATEGORY = (
        ("Indoor","Indoor"),
        ("Outdoor","Outdoor"),
    )


    name =models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200,null=True,choices=CATEGORY)
    description = models.CharField(max_length=200,null=True)
    tags = models.ManyToManyField(Tags)
    date_created =models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name



class Order(models.Model):
    STATUS = (
        ("Pending","Pending"),
        ("Delivered","Delivered"),
        ("Out for delivery", "Out for delivery"),
    )

    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null = True,choices=STATUS)
    date_created =models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.product.name