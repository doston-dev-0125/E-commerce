from django.shortcuts import render,redirect
from .models import Category,Product,Order,Brand
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.http import HttpResponse


def index(request):
    category=Category.objects.all()
    categoryID=request.GET.get('category')
    brand=Brand.objects.all()
    brandID=request.GET.get('brand')
    
    if categoryID:
        product = Product.objects.filter(sub_category =categoryID).order_by('-id')
    elif brandID:
        product = Product.objects.filter(brand = brandID).order_by('-id')
    else:
        product=Product.objects.all()
        
    
    
    
    context={
        'category':category,
        'product':product,
        'brand':brand,
    }
    return render(request,'index.html',context)

@login_required(login_url="/accounts/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/accounts/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_detail(request):
    return render(request, 'cart_detail.html')

    
def order_view(request):
    if request.method == "POST":
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        pincode=request.POST.get('pincode')
        cart=request.session.get('cart')
        uid=request.session.get('_auth_user_id')
        user=User.objects.get(pk=uid)
        
        for i in cart:
            a=float(cart[i]['price'])
            b=int(cart[i]['quantity'])
            total=a * b
            order=Order(
                user=user,
                product=cart[i]['name'],
                price=cart[i]['price'],
                quantity=cart[i]['quantity'],
                image=cart[i]['image'],
                pincode=pincode,
                address=address,
                phone=phone,
                total=total
            )
            order.save()
        request.session['cart'] = {}
        return redirect('index')
    return HttpResponse('save')
    
def your_order(request):
    uid=request.session.get('_auth_user_id')
    user=User.objects.get(pk=uid)
    
    order=Order.objects.filter(user=user)
    
    context={
        'order': order,
    }
    return render(request,'order.html',context)

def product_detail(request , id):
    product=Product.objects.filter(id = id).first()
    category=Category.objects.all()
    brand=Brand.objects.all()
    context ={
        'product': product,
        'category': category,
        'brand':brand,
    } 
    
    return render(request,'product_detail.html',context)

def search_view(request):
    query=request.GET['query']
    product=Product.objects.filter( name__icontains = query)
    context={
        'product':product,
    }
    return render(request,'search.html',context)