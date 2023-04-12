import logging

from django.http import HttpRequest
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.views import APIView
from src.auth.decorators.permission_required import login_required
from src.repository.cart_repository import CartRepository

logger = logging.getLogger(__name__)


class CustomSchema(AutoSchema):
    def get_serializer(self, path, method):
        return CartSerializer()


class ReportSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    price = serializers.FloatField()
    product_id = serializers.IntegerField()


class CartSerializer(serializers.Serializer):
    reports = ReportSerializer(many=True)


class CartList(APIView):
    schema = CustomSchema()

    @login_required
    def get(self, request: HttpRequest, format=None):
        print(request.user)
        repository = CartRepository(request.user, request.session)
        cart = repository.get_or_create()
        serializer = CartSerializer(cart)
        return Response(serializer.data)
