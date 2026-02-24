from django.db import models

class ItemModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expires_at = models.DateField()

    amount = models.IntegerField(default=0)
    price_per_one_item =models.DecimalField(max_digits=10, decimal_places=2, default=0)
    full_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def save(self, *a, **kw):
        self.full_price = self.price_per_one_item * self.amount
        super().save(*a, **kw)

    
    def __str__(self):
        return f'Item: {self.name}; price: {self.price_per_one_item}'