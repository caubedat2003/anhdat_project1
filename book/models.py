from django.db import models
from mongoengine import Document, StringField, DecimalField, IntField
from product.models import Product
class Book(Product):
    author = StringField(max_length=255, required=True)
    category = StringField()
    image = StringField()

    def is_in_stock(self):
        return self.stock > 0

    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            self.save()
            return True
        return False

    def get_discounted_price(self, discount_percentage):
        return self.price * (1 - discount_percentage / 100)

    def __str__(self):
        return f"{self.title} by {self.author}"
    
#book = Book.objects.create(title = "So Do", author = "Vu Trong Phung", description = "interesting story", price = 10, stock = 200, category = "Novel")