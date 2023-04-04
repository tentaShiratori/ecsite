from src.auth.decorators.permission_required import login_required, permission_required
from src.di import injector
from rest_framework import serializers
from rest_framework.schemas.openapi import AutoSchema
from src.drivers.file_uploader import FileUploader
from ..models import Product, User
from django.http import Http404, HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
import logging
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import QueryDict
from typing import cast
from src.models import Seler, Admin

logger = logging.getLogger(__name__)


class CustomSchema(AutoSchema):
    def get_serializer(self, path, method):
        return ProductSerializer()

    def map_field(self, field):
        if isinstance(field, serializers.ImageField):
            return {"type": "string"}
        return super().map_field(field)

    def map_serializer(self, serializer):
        result = super().map_serializer(serializer)
        result["required"].append("image")
        result["required"].append("pk")
        return result


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Product
        fields = ["pk", "name", "description", "image", "price", "user"]

    def to_representation(self, instance: Product):
        res = super().to_representation(instance)
        file_uploader = injector.get(FileUploader)
        res["image"] = file_uploader.host + instance.image
        return res

    def create(self, validated_data):
        image: InMemoryUploadedFile = validated_data["image"]
        file_uploader = injector.get(FileUploader)
        file_uploader.run(image, image.name)
        validated_data["image"] = image.name
        return super().create(validated_data=validated_data)


class ProductList(APIView):
    schema = CustomSchema()

    def get(self, request: HttpRequest, format=None):
        products = Product.objects.all()

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    @permission_required([Admin, Seler])
    def post(self, request: Request, format=None):
        user: User = User.objects.first()
        if user == None:
            Response(status=status.HTTP_404_NOT_FOUND)
        data = cast(QueryDict, request.data)
        data.appendlist("user", user.pk)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    schema = CustomSchema()

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:  # type: ignore
            raise Http404

    def get(self, request: Request, pk: int):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    @permission_required([Admin, Seler])
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_required([Admin, Seler])
    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
