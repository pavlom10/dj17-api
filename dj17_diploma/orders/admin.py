from django.contrib import admin
from .models import Order, OrderPositions


class OrderPositionsInline(admin.TabularInline):
    model = OrderPositions
    # formset = OrderPositionsInlineFormset
    # ordering = ('-is_main',)
    # extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ordering = ['-created_at']
    list_display = ('__str__', 'user', 'total_quantity', 'created_at')
    inlines = (OrderPositionsInline, )

    def total_quantity(self, obj):
        positions = obj.positions.all()
        total_quantity = 0
        for position in positions:
            order_positions = OrderPositions.objects.get(order=obj, product=position)
            total_quantity += order_positions.quantity
        return total_quantity