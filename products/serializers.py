from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=3, max_length=100, trim_whitespace=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at']
        read_only_fields = ['id', 'created_at']


class ProductSerializer(serializers.ModelSerializer):
    category_detail = CategorySerializer(source = 'category', read_only = True)
    name = serializers.CharField(min_length=3, max_length=100, trim_whitespace=True)
    price= serializers.IntegerField(min_value = 1)


    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'is_active', 'category', 'category_detail', 'created_at']
        read_only_fields = ['id', 'created_at']
        
