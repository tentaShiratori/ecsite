import boto3
from injector import provider, Module, singleton
from django.conf import settings
from mypy_boto3_cognito_idp import CognitoIdentityProviderClient
from mypy_boto3_s3 import S3Client


class AWSModule(Module):
    @singleton
    @provider
    def s3_client(self) -> S3Client:
        return boto3.client("s3", endpoint_url=settings.S3_ENDPOINT)

    @singleton
    @provider
    def cognito_client(self) -> CognitoIdentityProviderClient:
        return boto3.client("cognito-idp", region_name="ap-northeast-1")
