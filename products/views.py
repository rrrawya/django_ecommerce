from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,ProductDetail
from .forms import ContactForm,RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import ProductSerializer, ProductDetailSerializer
# Create your views here.
from django.shortcuts import render




class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer



class ProductDetailsViewSet(viewsets.ModelViewSet):
    queryset=ProductDetail.objects.all()
    serializer_class=ProductDetailSerializer




class ProductCreateAPIView(APIView):

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





def list(request):
    print(request.session['m'])
    tax=request.session['price']
    request.session['value']="welcome"
    tax=tax+(tax*(0.15))
    request.session['price']=tax
    cat_id=request.GET.get("category_id")
    user=request.COOKIES.get('user')
    print(user)
    _search=request.GET.get("search")

    products=Product.objects.all()
    if cat_id:
        f_product=Product.objects.filter(Category_id=cat_id)
    else :
        f_product=Product.objects.all()

        

    if _search:
        products=Product.objects.filter(name__icontains=_search)

    context={
        "prod":products,
        
       
    }

    
    return render(request,"products/list.html",context)



def product_details(request,product_id):

    product = get_object_or_404(
        Product.objects.select_related('details'),
        id=product_id
    )
    print(Product)

    context={
        "product":product
    }

    return render(request,"products/product_info.html",context)

def cart_view(request):
    cart=request.session.get('cart',{})  # جلب المنتجات 
    context={
        "cart":cart
    }
    return render(request,"products/cart.html",context)

@login_required
def checkout(request):
    
    return render(request,"products/checkout.html")

def send_email(request,email):

    subject="شركة المنار للتسويق الإليكتروني"
    to_email=[email]
    context={
        'user_name':"عميلنا العزيز",
        'year':datetime.now().year,
    }

    html_content=render_to_string("emails/email_send.html",context)
    text_content=strip_tags(html_content)

    email=EmailMultiAlternatives(
        subject,
        text_content,
         settings.EMAIL_HOST_USER,
         to_email



    )

    email.attach_alternative(html_content, "text/html")

    email.send( fail_silently=False)

    return HttpResponse("تم ارسال البريد الإليكتروني بنجاح")
    
    # send_mail(
    #     'شركة المنار للتسويق الإليكتروني',
    #     'تم استلام بريدك الإليكتروني وسيم معالجة طلبك خلال ثلاثة ايام عمل شكراً لتواصلكم',
    #     settings.EMAIL_HOST_USER,
    #     [email],
    #     fail_silently=False

    # )



















def add_to_cart(request,pid):
   
    prod = get_object_or_404(Product, pk=pid)

    cart=request.session.get('cart',{})  # جلب المنتجات 
   
    #product_id=str(Product.id)

    if pid in cart:
        cart[pid]['quantity'] +=1
    else:
        cart[pid]={
            'id': pid,
            'name': prod.name,
            'price': float(prod.price),
            'quantity':1

        }

    request.session['cart']=cart
    
    counter=request.session.get('cart_count',0)
    counter +=1
    request.session['cart_count']=counter
    return redirect(request.META.get('HTTP_REFERER', '/')) 


def auth_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("checkout")
    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {"form": form})




def register(request):
    pass

def contact(request):
    form=ContactForm()
    
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
           email=form.cleaned_data['email']
           send_email(request,email)
           # حفظ البيانات في الجدول 
           messages.success(request, 'تم إرسال رسالتك بنجاح! شكراً لتواصلك معنا.')
           messages.success(request, 'سعداء لتواصلك معنا ')
           return render(request,'contact.html',{'form':ContactForm(),
                'success':True
                })
        else:
             messages.error(request, 'يرجى التأكد من صحة البيانات المرسلة ')
        

        form=ContactForm()

    return render(request,'contact.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect("/")


def auth_register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect("list")
    else:
        form=RegisterForm()
    return render(request,"accounts/register.html",{"form":form})

    