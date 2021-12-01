from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls.conf import path
from perfiles.models import Perfil
from products.models import Category, Product

# Create your views here.
@login_required
def list(request):
    list = Product.objects.all()
    list2= Category.objects.all()
    return render(request,'products/index.html', {"list": list,"list2":list2})

@login_required   
def filter_by_category(request,id):
    list=Product.objects.filter(category=id)
    list2=Category.objects.all()
    return render(request, 'products/index.html', {"list": list,"list2":list2})

@login_required
def register_product(request):
    if request.method == "GET":
        list=Category.objects.all()
        return render(request, 'products/sell.html', {"list": list})
    name_ = request.POST["name"]
    description_ = request.POST["description"]
    price_ = request.POST["price"]
    discount_ = request.POST["discount"]
    print(name_)
    file_ = request.FILES["file"]
    category_=Category.objects.get(id=request.POST["category"])
    id_seller_ =  Perfil.objects.get(usuario_id=request.user.id)


    product= Product(name=name_, description=description_, path=file_,price=price_,discount=discount_,category=category_,id_seller=id_seller_,)
    product.save()
    return redirect('products:list')

@login_required
def detail(request,id):
    item=Product.objects.get(pk=id)
    return render(request,'products/detail.html',{"item":item})
