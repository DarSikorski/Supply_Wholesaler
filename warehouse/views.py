from multiprocessing import context
from django.shortcuts import render
from .models import *

#https://docs.djangoproject.com/en/4.0/ref/models/querysets/

def warehouse(request):
    context = {}
    return render(request, 'warehouse/main.html', context)

def items(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'warehouse/items.html', context)

def order(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_order_total':0, 'get_order_items':0}
    context = {'items':items, 'order':order}
    return render(request, 'warehouse/order.html', context)