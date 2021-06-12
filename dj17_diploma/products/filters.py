from django_filters import rest_framework as filters
from .models import Product
from django.db.models import Q


def multiple_search(queryset, name, value):
    queryset = queryset.filter(Q(name__icontains=value) | Q(description__icontains=value))
    return queryset


class ProductFilter(filters.FilterSet):

    search = filters.CharFilter(label='name or description', method=multiple_search)
    price_from = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_to = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ('price', 'name', 'description')
