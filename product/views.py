from django.contrib.auth.decorators import login_required
import iyzipay
from django.shortcuts import render, redirect
import datetime
from .forms import ShippingAddress
from .models import *
from payment import urls


api_key = 'sandbox-IOUkLip1LwPwAX0IZhTd10G31xg9f53Z'
secret_key = 'sandbox-uI0rttXtNUYyZlpmZN6WS2PSvnhSmqGV'
base_url = ' https://sandbox-api.iyzipay.com'

options = {
    'api-key':api_key,
    'secret-key':secret_key,
    'base-url':base_url,
}

libToken = list()


# Create your views here.
def homePage(request):
    control = request.user.is_authenticated

    if control:
        customer = request.user.customer
        user = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        cartItems = order.get_cart_items
    else:

        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
        user = request.user

    categories = Category.objects.all()

    products = Product.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'cartItems': cartItems,
        'user': user,
        'control': control,

    }

    return render(request, 'home.html', context)


def detailPage(request, id):
    if request.user.is_authenticated:
        customer = request.user.customer
        user = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        cartItems = order.get_cart_items
    else:

        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
        user = request.user

    product = Product.objects.get(id=id)

    control = request.user.is_authenticated

    if product.content is not None:
        contents = product.content.split()
    else:
        contents = ""

    context = {
        'cartItems': cartItems,
        'contents': contents,
        'product': product,
        'user': user,
        'control': control,
    }
    return render(request, 'detail.html', context)


def cartPage(request):
    control = request.user.is_authenticated
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        user = request.user
        cartItems = order.get_cart_items
    else:
        items = []
        order = {
            'get_cart_total': 0,
            'get_cart_items': 0,
            'shipping': False,
        }
        user = request.user

    context = {
        'items': items,
        'order': order,
        'user': user,
        'control': control,

    }

    return render(request, 'cart.html', context)


def checkoutPage(request):
    control = request.user.is_authenticated
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    form = ShippingAddress
    user = request.user

    context = {
        'items': items,
        'order': order,
        'form': form,
        'user': user,
        'control': control,
    }

    return render(request, 'checkout.html', context)


def add_item(request, id):
    customer = request.user.customer
    product = Product.objects.get(id=id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    orderItem.quantity = orderItem.quantity + 1
    orderItem.save()

    # her zaman bi onceki url ye yonlendirmesi icin
    url = request.META.get('HTTP_REFERER')
    return redirect(url)


def remove_item(request, id):
    product = Product.objects.get(id=id)
    customer = request.user.customer
    order, created = Order.objects.get_or_create(complete=False, customer=customer)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    orderItem.quantity = orderItem.quantity - 1
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return redirect('cart')


def remove_items(request, id):
    product = Product.objects.get(id=id)
    customer = request.user.customer
    order, created = Order.objects.get_or_create(complete=False, customer=customer)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    orderItem.delete()

    return redirect('cart')


@login_required
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()

    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    total = order.get_cart_total
    order.transaction_id = transaction_id
    order.complete = True
    order.save()
    if request.method == 'POST':
        form = ShippingAddress(request.POST)
        if form.is_valid():
            address = request.POST.get('address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            zipcode = request.POST.get('zipcode')
            email = request.POST.get('email')
            ShippingAdress.objects.create(customer=customer, order=order, address=address, city=city, state=state,
                                          zipcode=zipcode, email=email)

    return redirect('payment')


def categoryList(request, id):
    control = request.user.is_authenticated

    if control:
        customer = request.user.customer
        user = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        cartItems = order.get_cart_items
    else:

        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
        user = request.user

    categories = Category.objects.all()

    products = Product.objects.filter(category_id=id)

    context = {
        'products': products,
        'categories': categories,
        'cartItems': cartItems,
        'user': user,
        'control': control,

    }

    return render(request, 'categoryPage.html', context)
