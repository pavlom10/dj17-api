from django.db import models
from products.models import Product


class Collection(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    products = models.ManyToManyField(Product, related_name='collections')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Collection'
        verbose_name_plural = 'Collections'

    def __str__(self):
        return self.name
