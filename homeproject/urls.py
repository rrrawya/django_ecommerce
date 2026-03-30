"""
URL configuration for homeproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from category import views as cat
from products import views as prod

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cat.index, name='index'),
    path('list/', prod.list, name='list'),
    path('add_to_cart/<int:pid>', prod.add_to_cart, name='add_to_cart'),
    path('details/<int:product_id>/', prod.product_details, name='details'),
    path('cart/', prod.cart_view, name='cart'),
    path('checkout/', prod.checkout, name='checkout'),
    path('login/', prod.auth_login, name='login'),
    path('register/', prod.auth_register, name='register'),
    path('contact/', prod.contact, name='contact'),
    path('logout/', prod.logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)