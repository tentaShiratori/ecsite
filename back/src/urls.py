from django.urls import include, path
from .views import products
from .views import register

urlpatterns = [
    path("register/client/", register.RegisterClientView.as_view()),
    path("products/", products.ProductList.as_view()),
    path("products/<int:pk>/", products.ProductDetail.as_view()),
]
