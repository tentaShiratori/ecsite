from rest_framework import routers, serializers, viewsets
from rest_framework.schemas.openapi import AutoSchema
from ..models import Product
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status


class CustomSchema(AutoSchema):
    def get_serializer(self, path, method):
        return ProductSerializer()

    def map_serializer(self, serializer):
        result = super().map_serializer(serializer)
        result["required"].append("image")
        return result


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Product
        fields = ["name", "description", "image", "price"]

    def get_image(self, obj):
        return obj.image.url


class ProductList(APIView):
    schema = CustomSchema()

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    schema = CustomSchema()

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request: Request, pk: int):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
