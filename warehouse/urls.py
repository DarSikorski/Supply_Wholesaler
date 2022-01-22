from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.warehouse, name = "warehouse"),
    path('auth/', include('djoser.urls.jwt')),
    path('items/', views.items, name="items"),
]