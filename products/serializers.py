from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at']
        read_only_fields = ['id', 'created_at']


class ProductSerializer(serializers.ModelSerializer):
    category_detail = CategorySerializer(source = 'category', read_only = True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'is_active', 'category', 'category_detail', 'created_at']
        read_only_fields = ['id', 'created_at']