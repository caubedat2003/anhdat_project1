from django.db import models
from product.models import Product
from mongoengine import Document, StringField, DecimalField, IntField

class Shoes(Product):
    brand = StringField()
    size = StringField()
    image = StringField()

    def __str__(self):
        return f"{self.title} - {self.brand} - {self.size} "

#shoe = Shoes.objects.create(title = "Pata", brand = "Thuong Dinh", description = "legendary shoe", price = 5, stock = 400, size = "40")