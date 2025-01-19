from django.db import models
from orders.models import Order

class SalesReport(models.Model):
    date = models.DateField()
    total_sales = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Sales Report for {self.date}"

    @staticmethod
    def generate_report(date):
        total_sales = Order.objects.filter(created_at__date=date).aggregate(models.Sum('total_price'))['total_price__sum']
        return SalesReport.objects.create(date=date, total_sales=total_sales)
