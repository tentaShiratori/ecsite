from src.auth.decorators.permission_required import login_required, permission_required
from src.di import injector
from rest_framework import serializers
from rest_framework.schemas.openapi import AutoSchema
from src.drivers.file_uploader import FileUploader
from ...models import Report, User
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
        return ReportSerializer()


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ["id"]


class ReportList(APIView):
    schema = CustomSchema()

    def get(self, request: HttpRequest, format=None):
        return Response("hello")

    def put(self, request: HttpRequest, format=None):
        return Response(status=status.HTTP_200_OK)
