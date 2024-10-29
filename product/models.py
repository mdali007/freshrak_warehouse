from django.db import models
from django.utils import timezone
from datetime import timedelta


class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    bought_price = models.DecimalField(max_digits=10, decimal_places=2)
    bought_date = models.DateField()
    market_price_today = models.DecimalField(max_digits=10, decimal_places=2)
    expiry_date = models.DateField(null=True, blank=True)
    low_stock_alert_threshold = models.IntegerField(default=10)  # adjust as needed

    def __str__(self):
        return self.name

    @property
    def is_expiring_soon(self):
        """Returns True if the product is close to expiring, False otherwise."""
        if self.expiry_date:
            return timezone.now().date() > self.expiry_date - timedelta(days=7)
        return False

    @property
    def is_low_stock(self):
        """Returns True if quantity is below the alert threshold."""
        return self.quantity <= self.low_stock_alert_threshold
