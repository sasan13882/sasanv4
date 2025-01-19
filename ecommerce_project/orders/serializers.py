from rest_framework import serializers
from .models import Order, OrderItem
from shop.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'order_number', 'total_payment', 'shipping_price', 'tax_price', 'is_delivered', 'is_paid', 'date_created', 'date_paid', 'items']
