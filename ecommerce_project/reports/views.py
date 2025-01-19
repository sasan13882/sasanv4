from django.shortcuts import render
from .models import SalesReport

def generate_sales_report(request):
    date = request.GET.get('date')
    report = SalesReport.generate_report(date)
    return render(request, 'reports/sales_report.html', {'report': report})
