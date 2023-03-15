from django.urls import include, path
from .views import products
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path("products/", products.ProductList.as_view()),
    path("products/<int:pk>/", products.ProductDetail.as_view()),
]
