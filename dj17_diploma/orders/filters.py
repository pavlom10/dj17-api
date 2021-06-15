from django_filters import rest_framework as filters
from .models import Order, OrderStatusChoices
from products.models import Product

class OrderFilter(filters.FilterSet):
    status = filters.ModelMultipleChoiceFilter(
        to_field_name='status',
        queryset=Order.objects.all()
    )
    total_price = filters.NumberFilter(field_name='total_price')
    created_at = filters.DateFromToRangeFilter()
    updated_at = filters.DateFromToRangeFilter()
    positions = filters.ModelMultipleChoiceFilter(
        to_field_name='id',
        queryset=Product.objects.all()
    )

    class Meta:
        model = Order
        fields = ('status', 'total_price', 'created_at', 'updated_at')
