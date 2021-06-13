from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ReviewSerializer
from .models import Review
from .filters import ReviewFilter


class UserIsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class ReviewViewSet(viewsets.ModelViewSet):
    """ ViewSet для отзывов """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filterset_class = ReviewFilter

    def get_permissions(self):
        """ Получение прав для действий. """
        if self.action in ['destroy', 'update', 'partial_update']:
            return [permissions.IsAuthenticated(), UserIsOwner()]
        elif self.action == 'create':
            return [permissions.IsAuthenticated()]
        return []
