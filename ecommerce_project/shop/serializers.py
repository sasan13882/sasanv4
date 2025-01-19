from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image', 'active']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'image', 'description', 'price', 'original_price', 'sale_price', 'category', 'stock', 'min_order_quantity', 'shipping_info', 'created_at', 'updated_at']
