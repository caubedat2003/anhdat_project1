from django.db import models
from mongoengine import Document, StringField, DecimalField, IntField
from product.models import Product

class Mobile(Product):
    brand = StringField()
    spec = StringField()
    image = StringField()

    def __str__(self):
        return f"{self.brand} - {self.title} - ${self.price}"

#mobile = Mobile.objects.create(title = "Iphone 11", brand = "Apple", description = "Mid-tier iphone", spec = "128GB - 4GB RAM - A13 Bionic chip", price = 500, stock = 1200)