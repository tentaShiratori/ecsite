from django.urls import include,path
from . import views
from rest_framework import routers, serializers, viewsets
from .views import ProductViewSet
router = routers.DefaultRouter()
router.register(r'', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]