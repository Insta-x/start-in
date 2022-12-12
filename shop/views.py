from django.shortcuts import render
from .models import Product, Cart, CartItems, DeliveryAdress
from django.http import JsonResponse
import json

# Fungsi register, login, logout
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from shop.forms import AddressForm
from django.contrib.auth.decorators import login_required

from authentication.forms import NormalUserCreationForm

from django.http import HttpResponse
from django.core import serializers

# Create your views here.

# Fungsi register, login, logout

# def register(request):
#     form = NormalUserCreationForm()

#     if request.method == "POST":
#         form = NormalUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Akun telah berhasil dibuat!')
#             return redirect('shop:login')
    
#     context = {'form':form}
#     return render(request, 'register.html', context)

# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('shop:homepage')
#         else:
#             messages.info(request, 'Username atau Password salah!')
#     context = {}
#     return render(request, 'login.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            return redirect('shop:homepage')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

# def logout_user(request):
#     logout(request)
#     return redirect('shop:login')






# Fungsi home dari shop
def homepage(request):
    context = {
        'username' : request.user.username,
        
    }
    return render(request, 'homepage.html', context)

# Fungsi clothing dan accessories menampilkan halaman produk
def clothing(request):

    # if request.user.is_authenticated:
    # Munculkan angka di cart
    if request.user.is_authenticated:
        customer = request.user
        cart, created = Cart.objects.get_or_create(owner=customer, completed=False)
        cartitems = cart.cartitems_set.all()
    else:
        cart = []
        cartitems = []
        cart = {'cartquantity': 0}

    products = Product.objects.filter(category="clothing")
    context = {'products':products, 'cart':cart, 'cartitems':cartitems}
    return render (request,'clothing.html', context)

def accessories(request):
    if request.user.is_authenticated:
        customer = request.user
        cart, created = Cart.objects.get_or_create(owner=customer, completed=False)
        cartitems = cart.cartitems_set.all()
    else:
        cart = []
        cartitems = []
        cart = {'cartquantity': 0}

    products = Product.objects.filter(category="accessories")
    context = {'products':products, 'cart':cart, 'cartitems':cartitems}
    return render (request,'accessories.html', context)


# Fungsi cart menghandle keranjang belanja
def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        cart, created = Cart.objects.get_or_create(owner=customer, completed=False)
        cartitems = cart.cartitems_set.all()
    else:
        cart = []
        cartitems = []
        cart = {'cartquantity': 0}
    context = {'cart': cart, 'cartitems': cartitems}
    return render (request,'cart.html', context)

def updateCart(request):
    data = json.loads(request.body)
    
    # Ambil dari js file
    product_id = data['product_id']
    action = data['action']

    if request.user.is_authenticated:
        customer=request.user
        product = Product.objects.get(product_id=product_id)
        cart,created = Cart.objects.get_or_create(owner=customer, completed=False)
        cartitems,created = CartItems.objects.get_or_create(product=product, cart=cart)

        if action == 'add':
            cartitems.quantity += 1
        cartitems.save()


        # Gunakan AJAX untuk update angka di cart sanpa reload page
        qty = {
            'quantity' : cart.cartquantity
        }
        

    return JsonResponse(qty, safe=False)

# Handle update quanitity dari input type number page cart
# mirip updatecart
def updateQuantity(request):
    data = json.loads(request.body) # Ambil data dari const data di cart.js
    inputval = int(data['in_val'] )
    product_id = data['p_id']
    if request.user.is_authenticated:
        customer = request.user
        product = Product.objects.get(product_id= product_id)
        cart, created = Cart.objects.get_or_create(owner=customer, completed=False)
        cartitems, created = CartItems.objects.get_or_create(product=product, cart=cart)

        # Send data ke backend
        cartitems.quantity = inputval 
        cartitems.save()

        update = {
            'subtotal' : cartitems.subtotal,
            'grandtotal' : cart.grandtotal,
            'quantity' : cart.cartquantity
        }

    return JsonResponse(update,safe=False)


# Handle Checkout
@login_required(login_url='/auth/login')
def checkout(request):
    data = DeliveryAdress.objects.filter(user=request.user)
    context = {
    'username' : request.user.username,
    'data' : data,
    
    }
    return render(request, "checkout.html",context)

def add_address(request):
    form = AddressForm(request.POST)
    if form.is_valid() and request.method == "POST":
        DeliveryAdress.objects.create(street=form.cleaned_data["street"], city=form.cleaned_data["city"], 
        province=form.cleaned_data["province"], postal=form.cleaned_data["postal"], user=request.user)

        return redirect("shop:checkout")
    form = AddressForm()
    return render(request, "add-address.html", context={"form":form})

def order_done(request):
    context = {
        'username' : request.user.username
    }
    return render(request, 'done.html', context)


# Membuat sebuah fungsi yang menerima parameter request (JSON)
def request_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Fungsi tambah alamat dari flutter
@login_required(login_url='/auth/login/')
def api_add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            DeliveryAdress.objects.create(street=form.cleaned_data["street"], city=form.cleaned_data["city"], 
            province=form.cleaned_data["province"], postal=form.cleaned_data["postal"], user=request.user)

            return JsonResponse({
                'status' : 'Success',
            }, status=200)

        return JsonResponse({
            'status' : 'Failed',
            'Message' : 'Invalid Requests'
        }, status=401)


