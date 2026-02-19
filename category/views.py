from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Category
# Create your views here.

# def index(request):
    
#     categories = [
#         {"id": 1, "name": "Electronics"},
#         {"id": 2, "name": "Clothes"},
#         {"id": 3, "name": "Books"},
#         {"id": 4, "name": "Sports"},
#         {"id": 5, "name": "Home"},
#     ]

#     context={
#         'cat':categories
#     }

#     return render(request,'category/index.html',context)

y=100 #gloobal


def index(request):
    request.session['price']=1000
    request.session['m']="شهر مبارك"
    categories=Category.objects.all()
    print(categories)
    context={
        'cat':categories,
       
    }

    x=10  # Local

    response= render(request,'category/index.html',context)
    response.set_cookie(
        key="user",
        value="saad",
        max_age=172800
    )
    return response


def get_name(request):
    print(y)


    