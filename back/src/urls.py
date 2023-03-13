from django.urls import include,path
from . import views
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
]