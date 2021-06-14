from django.contrib import admin
from .models import Collection
from products.models import Product


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    # list_display = ('name', 'price', 'created_at')
    pass
