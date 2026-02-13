from django.shortcuts import render

# Create your views here.


def list(request):
    products = [
    # الفئة 1: إلكترونيات
    {"id": 1, "name": "MacBook Pro", "category_id": 1, "price": 2500, "image": "https://images.unsplash.com/photo-1517336714460-4c50d917842a?q=80&w=500"},
    {"id": 2, "name": "iPhone 15", "category_id": 1, "price": 999, "image": "https://images.unsplash.com/photo-1510557880182-3d4d3cba35a5?q=80&w=500"},
    {"id": 3, "name": "Sony Headphones", "category_id": 1, "price": 350, "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=500"},
    {"id": 4, "name": "Samsung Monitor 27'", "category_id": 1, "price": 300, "image": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?q=80&w=500"},
    
    # الفئة 2: ملابس
    {"id": 5, "name": "Cotton T-shirt", "category_id": 2, "price": 25, "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?q=80&w=500"},
    {"id": 6, "name": "Leather Jacket", "category_id": 2, "price": 120, "image": "https://images.unsplash.com/photo-1521223890158-f9f7c3d5d504?q=80&w=500"},
    {"id": 7, "name": "Blue Jeans", "category_id": 2, "price": 45, "image": "https://images.unsplash.com/photo-1542272604-787c3835535d?q=80&w=500"},
    {"id": 8, "name": "Winter Scarf", "category_id": 2, "price": 15, "image": "https://images.unsplash.com/photo-1520903920243-00d872a2d1c9?q=80&w=500"},
    
    # الفئة 3: كتب
    {"id": 10, "name": "Atomic Habits", "category_id": 3, "price": 22, "image": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?q=80&w=500"},
    {"id": 11, "name": "Python Programming", "category_id": 3, "price": 40, "image": "https://images.unsplash.com/photo-1515879218367-8466d910aaa4?q=80&w=500"},
    
    # الفئة 4: رياضة
    {"id": 13, "name": "Adidas Football", "category_id": 4, "price": 35, "image": "https://images.unsplash.com/photo-1574629810360-7efbbe195018?q=80&w=500"},
    {"id": 14, "name": "Yoga Mat", "category_id": 4, "price": 20, "image": "https://images.unsplash.com/photo-1592432678016-e910b452f9a2?q=80&w=500"},
    
    # الفئة 5: أدوات منزلية
    {"id": 17, "name": "Espresso Machine", "category_id": 5, "price": 150, "image": "https://images.unsplash.com/photo-1517668808822-9ebb02f2a0e6?q=80&w=500"},
    {"id": 18, "name": "Air Fryer", "category_id": 5, "price": 110, "image": "https://images.unsplash.com/photo-1626075133930-07755a50787e?q=80&w=500"},
]
    
   

    cat_id=request.GET.get('category_id')

    if cat_id:
        filterd_products=[p for p in products  if p["category_id"]==int(cat_id)]
    else:
        filterd_products=products
    

    context={
        'prod':filterd_products
    }

    return render(request,'products/list.html',context)