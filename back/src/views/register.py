from django.http.request import HttpRequest
from src.models import Client, Admin, Seler, User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["sub", "email"]


class RegisterClientView(APIView):
    def post(self, request: HttpRequest):
        if request.auth is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        client = Client(sub=request.auth.sub, email=request.auth.email)
        client.save()
        serializer = UserSerializer(client)
        return Response(serializer.data)


class RegisterAdminView(APIView):
    def post(self, request: HttpRequest):
        if request.auth is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        client = Admin(sub=request.auth.sub, email=request.auth.email)
        client.save()
        serializer = UserSerializer(client)
        return Response(serializer.data)


class RegisterSelerView(APIView):
    def post(self, request: HttpRequest):
        if request.auth is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        client = Seler(sub=request.auth.sub, email=request.auth.email)
        client.save()
        serializer = UserSerializer(client)
        return Response(serializer.data)
