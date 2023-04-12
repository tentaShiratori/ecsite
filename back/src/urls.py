from django.urls import include, path

from .views import carts, products, register
from .views.carts import urls as cart_urls

urlpatterns = [
    path("carts/", include(cart_urls)),
    path("register/client/", register.RegisterClientView.as_view()),
    path("register/admin/", register.RegisterAdminView.as_view()),
    path("register/seler/", register.RegisterSelerView.as_view()),
    path("products/", products.ProductList.as_view()),
    path("products/<int:pk>/", products.ProductDetail.as_view()),
]
