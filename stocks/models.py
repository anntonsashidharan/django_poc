from django.db import models

# Create your models here.
class Stock(models.Model):
    stock_name = models.CharField(max_length=100)
    stock_price = models.CharField(max_length=20)
    stock_last_updated = models.DateTimeField(auto_now=True)
