from django.contrib import admin
from .models import Product


@admin.register(Product)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
