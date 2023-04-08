from django.core.management.base import BaseCommand, CommandError
from src.lib.aws import MyCognitoClient
from src.models import Product, User
from django.core.files import File
import boto3
from mypy_boto3_cognito_idp import CognitoIdentityProviderClient
from botocore.exceptions import ClientError


class Command(BaseCommand):
    help = "confirm user"

    def handle(self, *args, **options):
        if len(args) == 0:
            raise Exception("token must be passed")
        token = args[0]
        client = MyCognitoClient()
        claim = client.token_to_claim(token)
        print(claim)
