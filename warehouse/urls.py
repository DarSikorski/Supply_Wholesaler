from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.warehouse, name = "warehouse"),
    path('auth/', include('djoser.urls.jwt')),
    path('oferta/', views.items, name="items"),
    path('zamowienie/', views.order, name="order"),
]