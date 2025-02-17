from django.db import models
from customer.models import Customer
from book.models import Book  

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="cart_items")  
    product = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="cart_items")  
    quantity = models.PositiveIntegerField(default=1) 
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  
    added_at = models.DateTimeField(auto_now_add=True) 

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.product.price  
        super().save(*args, **kwargs)

    def update_quantity(self, new_quantity):
        if new_quantity > 0:
            self.quantity = new_quantity
            self.total_price = self.quantity * self.product.price
            self.save()
        else:
            self.delete()  

    def __str__(self):
        return f"{self.customer.username} - {self.product.title} (x{self.quantity})"

