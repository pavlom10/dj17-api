from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CollectionSerializer
from .models import Collection


class CollectionViewSet(viewsets.ModelViewSet):
    """ ViewSet для коллекций """
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]
        return []
