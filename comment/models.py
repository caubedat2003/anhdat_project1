from mongoengine import Document, ReferenceField, StringField, DateTimeField
from datetime import datetime
from customer.models import Customer  # Assuming the Customer model is in MySQL

class Comment(Document):
    product = ReferenceField('Product', required=True)  # Link to Product
    customer_id = StringField(required=True)  # Store customer ID as string (from MySQL)
    content = StringField(required=True, max_length=1000)
    created_at = DateTimeField(default=datetime.utcnow)

    meta = {'collection': 'comments'}
