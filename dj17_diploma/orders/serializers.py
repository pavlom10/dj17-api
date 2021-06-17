from rest_framework import serializers
from .models import Order, OrderPositions
from products.models import Product


class OrderPositionsSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        required=True
    )
    quantity = serializers.IntegerField(min_value=1, default=1)

    class Meta:
        model = OrderPositions
        fields = ('product', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    products = OrderPositionsSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'products', 'status', 'total_price', 'created_at', 'updated_at')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        products_data = validated_data.pop('products')

        total_price = 0
        for item in products_data:
            total_price += item['product'].price * item['quantity']
        validated_data['total_price'] = total_price
        order = Order.objects.create(**validated_data)

        for item in products_data:
            OrderPositions.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
            )
        return order