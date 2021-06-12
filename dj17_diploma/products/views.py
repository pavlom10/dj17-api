from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProductSerializer
from .models import Product
from .filters import ProductFilter


class ProductViewSet(viewsets.ModelViewSet):
    """ ViewSet для товара """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            return [permissions.IsAdminUser()]
        return []
