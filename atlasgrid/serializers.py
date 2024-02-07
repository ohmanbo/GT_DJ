# serializers.py
from rest_framework import serializers
from .models import grid

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = grid
        fields = '__all__'
