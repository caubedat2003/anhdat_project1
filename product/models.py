from mongoengine import Document, StringField, DecimalField, IntField

class Product(Document):
    title = StringField(max_length=255, required=True)
    description = StringField()
    price = DecimalField(precision=2)
    stock = IntField()

    meta = {'allow_inheritance': True}
    