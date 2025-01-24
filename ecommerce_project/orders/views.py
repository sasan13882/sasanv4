from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Order, OrderItem
from .serializers import OrderSerializer
from products.models import Product

# === Django Views for Template Rendering ===
@login_required
def create_order(request):
    """ ایجاد سفارش جدید از سبد خرید """
    cart_items = request.session.get('cart', [])
    if not cart_items:
        return redirect('cart')  # اگر سبد خرید خالی بود، بازگشت به صفحه‌ی سبد خرید

    # ایجاد سفارش جدید
    order = Order.objects.create(user=request.user, status='pending', total_price=_calculate_total(cart_items))
    
    # افزودن محصولات به سفارش
    for item in cart_items:
        product = Product.objects.get(id=item['product_id'])
        OrderItem.objects.create(order=order, product=product, quantity=item['quantity'], unit_price=product.price_rial)

    # پاک کردن سبد خرید پس از ثبت سفارش
    del request.session['cart']

    return redirect('order_detail', order_id=order.id)

def _calculate_total(cart_items):
    """ محاسبه‌ی مجموع قیمت اقلام در سبد خرید """
    return sum(Product.objects.get(id=item['product_id']).price_rial * item['quantity'] for item in cart_items)

@login_required
def order_list(request):
    """ نمایش لیست سفارشات برای کاربر وارد شده """
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})

# === DRF Views for API ===
class OrderListView(ListCreateAPIView):
    """ لیست سفارشات و ایجاد سفارش جدید از طریق API """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(RetrieveUpdateDestroyAPIView):
    """ مشاهده، به‌روزرسانی و حذف یک سفارش خاص از طریق API """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
