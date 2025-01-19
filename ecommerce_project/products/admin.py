from django.contrib import admin
from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['code', 'description', 'price_rial', 'category']
    search_fields = ['code', 'description']
    list_filter = ['category']

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
