from django.urls import path
from .views import CartView, CartItemView

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/<int:pk>/', CartItemView.as_view(), name='cart-item'),
]
