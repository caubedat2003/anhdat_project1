from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128) 
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    def get_full_name(self): 
        return f"{self.first_name} {self.last_name}".strip()

    def get_username(self):
        return self.username

    def __str__(self):
        return self.get_full_name()