from typing import Optional, Any, cast
from django.contrib.auth.middleware import AuthenticationMiddleware
from django.http.request import HttpRequest

from django.utils.functional import SimpleLazyObject
from src.models import User
from src.di import injector
from src.drivers.aws.user_claim_resolver import UserClaimResolver
from django.contrib.auth.models import AnonymousUser


class CognitoAuthMiddleware(AuthenticationMiddleware):
    @staticmethod
    def get_auth_token(request: HttpRequest) -> Optional[str]:
        auth_token = request.headers.get("Authorization")

        if auth_token == None:
            return None
        arr = auth_token.split(" ")
        if len(arr) < 2:
            return None
        return arr[1]

    def authenticate(self, request):
        token = self.get_auth_token(request)

        try:
            if token == None:
                return AnonymousUser()
            claims = injector.get(UserClaimResolver).run(token)
            if claims == None:
                return AnonymousUser()
            user = User.objects.get(email=claims.username)
            return user
        except User.DoesNotExist:
            return AnonymousUser()

    def process_request(self, request):
        token = self.get_auth_token(request)
        if token == None:
            return
        request.claims = injector.get(UserClaimResolver).run(token)
        request.user = cast(Any, SimpleLazyObject(lambda: self.authenticate(request)))
