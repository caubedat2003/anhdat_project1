from django.db import models
from customer.models import Customer
from mobile.models import Mobile
from clothes.models import Clothes

class Order(models.Model):
    customer_id = models.UUIDField()
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    cart = models.ForeignKey('cart.Cart', on_delete=models.SET_NULL, null=True)
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

