import logging

from django.http import HttpRequest
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.views import APIView
from src.entities.cart import Report
from src.repository.cart_repository import CartRepository

logger = logging.getLogger(__name__)


class CustomSchema(AutoSchema):
    def get_request_serializer(self, path, method):
        return PostReportRequestSerializer()

    def get_response_serializer(self, path, method):
        return PostReportResponseSerializer()


class PostReportRequestSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    price = serializers.FloatField()
    product_id = serializers.IntegerField()


class PostReportResponseSerializer(PostReportRequestSerializer):
    pass


class ReportList(APIView):
    schema = CustomSchema()

    def get(self, request: HttpRequest, format=None):
        return Response("hello")

    def post(self, request: HttpRequest, format=None):
        serializer = PostReportRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        repository = CartRepository(request.user, request.session)
        cart = repository.get_or_create()
        report = Report(**serializer.validated_data)  # type: ignore
        cart.reports.append(report)
        repository.save(cart)
        return Response(
            status=status.HTTP_200_OK, data=PostReportResponseSerializer(report).data
        )
