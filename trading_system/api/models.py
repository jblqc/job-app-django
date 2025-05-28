from django.db import models

class Stock(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    company_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # current price

    def __str__(self):
        return f"{self.symbol} - {self.company_name}"

class Order(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)  # rename here

    def __str__(self):
        return f"{self.quantity} x {self.stock.symbol} at {self.price}"
