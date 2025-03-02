from django.db import models
from order.models import Order

class Shipping(models.Model):
    customer_id = models.UUIDField()
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE)
    address_id = models.UUIDField()
    method = models.CharField(
        max_length=50,
        choices=[
            ('giaohangtietkiem', 'Giao hàng tiết kiệm'),
            ('giaohangnhanh', 'Giao hàng nhanh'),
            ('j&texpress', 'J&T Express'),
            ('ninjavan', 'Ninja Van'),
            ('viettlepost', 'Viettle Post'),
        ],
        default='giaohangtietkiem'
    )

    def __str__(self):
        return f"Shipping for Order {self.order.id}"
