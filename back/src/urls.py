from django.urls import include, path
from .views import products
from .views import register
from .views import carts

urlpatterns = [
    path("cart/", carts.CartList.as_view()),
    path("register/client/", register.RegisterClientView.as_view()),
    path("register/admin/", register.RegisterAdminView.as_view()),
    path("register/seler/", register.RegisterSelerView.as_view()),
    path("products/", products.ProductList.as_view()),
    path("products/<int:pk>/", products.ProductDetail.as_view()),
]
