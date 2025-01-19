from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
