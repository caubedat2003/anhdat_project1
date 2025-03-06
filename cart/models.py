from django.db import models
from product.models import Product

class Cart(models.Model):
    customer_id = models.CharField(max_length=50)  # Ensure it's stored as a string
    product_id = models.CharField(max_length=24)  # Store MongoDB ObjectID as string
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        product = Product.objects(id=self.product_id).first()  # Get product from MongoDB
        if product:
            self.total_price = self.quantity * float(product.price)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Customer {self.customer_id} - Product {self.product_id} (x{self.quantity})"
