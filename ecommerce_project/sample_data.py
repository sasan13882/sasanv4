import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce_project.settings")
django.setup()

from products.models import Category, Product

# Insert categories
categories = [
    'Threaded Fittings',
    'Five-Layer Pipe',
    'NewPipe',
    'Elbow',
    'Compression Fittings',
    'Collector Cap',
    'Air Vent Parts',
    'Press Fittings',
    'Cap'
]

for category_name in categories:
    Category.objects.get_or_create(name=category_name)

# Insert products
products = [
    ('10407', 'Conversion Male Thread 4/3" to Female Thread 2/1" (Type B)', 248500, 'Threaded Fittings'),
    ('91216', 'NewPipe (PEX-AL-PEX) 16mm', 152200, 'Five-Layer Pipe'),
    # Add more products as needed...
]

for code, description, price_rial, category_name in products:
    category = Category.objects.get(name=category_name)
    Product.objects.get_or_create(code=code, description=description, price_rial=price_rial, category=category)