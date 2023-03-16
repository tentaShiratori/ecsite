from django.urls import include, path
from .views import products

urlpatterns = [
    path("products/", products.ProductList.as_view()),
    path("products/<int:pk>/", products.ProductDetail.as_view()),
]
