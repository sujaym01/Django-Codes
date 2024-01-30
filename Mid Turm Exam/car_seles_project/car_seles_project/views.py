from django.shortcuts import render
from car_sales_app.models import Car
from categories_app.models import Category



def home(request, category_slug = None):
    data = Car.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        data = Car.objects.filter(category  = category)
    categories = Category.objects.all()
    return render(request, 'home.html', {'data' : data, 'category' : categories})