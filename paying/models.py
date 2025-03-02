from django.db import models
from order.models import Order

class Paying(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(
        max_length=20,
        choices=[
            ('credit_card', 'Credit Card'),
            ('paypal', 'PayPal'),
            ('momo', 'MoMo'),
            ('bank_transfer', 'Bank Transfer'),
            ('cash_on_delivery', 'Cash on Delivery')
        ]
    )
    payment_status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('completed', 'Completed'),
            ('failed', 'Failed')
        ],
        default='pending'
    )
    transaction_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order {self.order.id} - {self.payment_status}"
