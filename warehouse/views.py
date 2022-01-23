from itertools import product
import json
import datetime
from multiprocessing import context
from django.shortcuts import render
from django.http import JsonResponse
from importlib_metadata import re
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
        order = {'get_order_total':0, 'shipping':False}
    context = {'items':items, 'order':order}
    return render(request, 'warehouse/order.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Dodano przedmiot', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_order_total:
            order.complete = True
        order.save()
        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )
    return JsonResponse('Dokonano wpłaty.', safe=False)