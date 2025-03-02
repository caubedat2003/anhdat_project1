from django.db import models
from mongoengine import Document, StringField, DecimalField, IntField
from product.models import Product
    
class Clothes(Product):
    brand = StringField()
    size = StringField()
    color = StringField()
    image = StringField()

    def __str__(self):
        return f"{self.title} - {self.brand} - {self.size} - {self.color}"
    
#clothes = Clothes.objects.create(title = "Ao phong", brand = "Candles", description = "White t-shirt", price = 30, stock = 600, size = "M", color = "White")