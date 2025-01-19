from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image_url = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price_rial = models.BigIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    related_products = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name
