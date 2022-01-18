from multiprocessing import context
from django.shortcuts import render



def warehouse(request):
    context = {}
    return render(request, 'warehouse/main.html', context)
