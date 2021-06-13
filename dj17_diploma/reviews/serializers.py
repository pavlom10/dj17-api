from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    mark = serializers.IntegerField(min_value=1, max_value=5, default=1)

    class Meta:
        model = Review
        fields = '__all__'