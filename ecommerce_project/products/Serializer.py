class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'image', 'description', 'price', 'original_price', 'sale_price', 'category', 'stock', 'min_order_quantity', 'shipping_info', 'created_at', 'updated_at', 'reviews']
class ProductSerializer(serializers.ModelSerializer):
    related_products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'related_products']
