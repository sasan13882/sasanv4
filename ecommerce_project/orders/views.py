from django.shortcuts import render, redirect
from .models import Order, OrderItem
from products.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def create_order(request):
    cart_items = request.session.get('cart', [])
    if not cart_items:
        return redirect('cart')  # Redirect to cart page if no items

    order = Order.objects.create(user=request.user, status='pending', total_price=calculate_total(cart_items))
    
    for item in cart_items:
        product = Product.objects.get(id=item['product_id'])
        OrderItem.objects.create(order=order, product=product, quantity=item['quantity'], unit_price=product.price_rial)
    
    return redirect('order_detail', order_id=order.id)

def calculate_total(cart_items):
    total = 0
    for item in cart_items:
        product = Product.objects.get(id=item['product_id'])
        total += product.price_rial * item['quantity']
    return total

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})
