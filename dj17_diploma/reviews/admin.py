from django.contrib import admin
from .models import Review


@admin.register(Review)
class ArticleAdmin(admin.ModelAdmin):
    # list_display = ('name', 'price', 'created_at')
    pass
