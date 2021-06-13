from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review')
    text = models.TextField()
    mark = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        unique_together = [['product', 'author']]

    def __str__(self):
        return str(self.product.name) + ' — ' + self.text[:50]

