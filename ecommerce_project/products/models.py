from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)  # اضافه شدن فیلد name
    description = models.TextField()
    price_rial = models.BigIntegerField()  # استفاده از BigIntegerField برای قیمت
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ایجاد
    updated_at = models.DateTimeField(auto_now=True)  # تاریخ بروزرسانی
    related_products = models.ManyToManyField('self', blank=True)  # قابلیت اضافه کردن محصولات مرتبط

    def __str__(self):
        return self.name
