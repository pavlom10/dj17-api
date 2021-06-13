from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class OrderStatusChoices(models.TextChoices):
    NEW = 'NEW', 'New'
    IN_PROGRESS = 'IN_PROGRESS', 'In progress'
    DONE = 'DONE', 'Done'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    positions = models.ManyToManyField(Product, related_name='orders', through='OrderPositions')
    status = models.TextField(
        choices=OrderStatusChoices.choices,
        default=OrderStatusChoices.NEW
    )
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderPositions(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Positions in order'

    # def __str__(self):
    #     return '{0}_{1}'.format(self.article, self.scope)

