from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_storage = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


