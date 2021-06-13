from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1, default=1)

    class Meta:
        model = Order
        fields = '__all__'