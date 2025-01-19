from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Cart
from .serializers import CartSerializer

class CartView(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemView(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
