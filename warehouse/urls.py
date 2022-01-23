from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.warehouse, name = "warehouse"),
    path('auth/', include('djoser.urls.jwt')),
    path('oferta/', views.items, name="items"),
    path('zamowienie/', views.order, name="order"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]