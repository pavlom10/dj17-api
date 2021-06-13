from django_filters import rest_framework as filters
from .models import Review


class ReviewFilter(filters.FilterSet):

    author_id = filters.NumberFilter(field_name='author')
    product_id = filters.NumberFilter(field_name='product')
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Review
        fields = ('author', 'product', 'created_at')