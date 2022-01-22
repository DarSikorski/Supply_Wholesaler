from multiprocessing import context
from django.shortcuts import render
from .models import *



def warehouse(request):
    context = {}
    return render(request, 'warehouse/main.html', context)

def items(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'warehouse/items.html', context)