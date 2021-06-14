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
    list_display = ('id', 'user', 'created_at')
    inlines = (OrderPositionsInline, )
