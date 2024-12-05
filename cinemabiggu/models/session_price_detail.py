from django.db import models


class SessionPriceDetail(models.Model):
    session = models.ForeignKey('cinemabiggu.Session', on_delete=models.CASCADE)
    full_price = models.DecimalField(max_digits=3, decimal_places=2)
    half_price = models.DecimalField(max_digits=3, decimal_places=2)
    fan_price = models.DecimalField(default=0.00, max_digits=3, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
