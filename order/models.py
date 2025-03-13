from django.db import models
from customer.models import Customer
from mobile.models import Mobile
from clothes.models import Clothes

class Order(models.Model):
    customer_id = models.CharField(max_length=50) 
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('delivering', 'Delivering'),
            ('finished', 'Finished'),
            ('canceled', 'Canceled')
        ],
        default='pending'
    )

    def __str__(self):
        return f"Order {self.id} - {self.customer.first_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product_id = models.CharField(max_length=100)  # MongoDB ObjectID stored as a string
    title = models.CharField(max_length=255)  # Store product name for reference
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.title} (x{self.quantity}) - Order {self.order.id}"