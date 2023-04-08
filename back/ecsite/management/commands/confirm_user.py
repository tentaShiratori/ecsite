from django.core.management.base import BaseCommand, CommandError
from src.models import Product, User
from django.core.files import File
import boto3
from mypy_boto3_cognito_idp import CognitoIdentityProviderClient


class Command(BaseCommand):
    help = "confirm user"

    def handle(self, *args, **options):
        client: CognitoIdentityProviderClient = boto3.client("cognito-idp")
        result = client.admin_confirm_sign_up(
            UserPoolId="ap-northeast-1_5rziSyaga",
            Username="foobar@gmail.com",
        )
        print(result)
