from rest_framework import viewsets
from rest_framework import permissions
from .serializers import OrderSerializer
from .models import Order
# from .filters import ReviewFilter


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.user == request.user


class OrderViewSet(viewsets.ModelViewSet):
    """ ViewSet для заказов """

    serializer_class = OrderSerializer
    # filterset_class = ReviewFilter

    def get_queryset(self):
        """ Filter objects so a user only sees his own stuff. If user is admin, let him see all. """
        if self.request.user.is_staff:
            return Order.objects.all()
        else:
            return Order.objects.filter(user=self.request.user)

    def get_permissions(self):
        """ Получение прав для действий. """
        if self.action in ['create', 'list']:
            return [permissions.IsAuthenticated()]
        elif self.action == 'retrieve':
            return [IsOwnerOrAdmin()]
        else:
            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]

