from django.shortcuts import render
from .models import Category
from products.models import Product

def index(request):
    
    products = Product.objects.all()[:3]

    categories = Category.objects.all()

    context = {
        'products': products,
        'cat': categories,
    }

    return render(request, 'category/index.html', context)