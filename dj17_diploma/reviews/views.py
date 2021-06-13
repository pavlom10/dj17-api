from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ReviewSerializer
from .models import Review
# from .filters import ProductFilter


class ReviewViewSet(viewsets.ModelViewSet):
    """ ViewSet для отзывов """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # filterset_class = ProductFilter

    # def get_permissions(self):
    #     if self.action in ['create', 'destroy', 'update', 'partial_update']:
    #         return [permissions.IsAdminUser()]
    #     return []
