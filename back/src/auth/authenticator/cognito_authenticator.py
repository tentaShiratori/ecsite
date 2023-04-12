from rest_framework.authentication import BaseAuthentication
from django.http.request import HttpRequest
from typing import Optional
from src.drivers.user_claims_resolver import UserClaimsResolver

from src.models.user import User
from src.di import injector


class CognitoAuthenticator(BaseAuthentication):
    @staticmethod
    def get_auth_token(request: HttpRequest) -> Optional[str]:
        auth_token = request.headers.get("Authorization")
        if auth_token == None:
            return None
        arr = auth_token.split(" ")
        if len(arr) < 2:
            return None
        return arr[1]

    def authenticate(self, request: HttpRequest):
        token = self.get_auth_token(request)
        if token == None:
            return (None, None)
        claims = injector.get(UserClaimsResolver).run(token)
        if claims is None:
            return (None, None)
        try:
            user = User.objects.get(sub=claims.sub)
            return (user, claims)
        except User.DoesNotExist:  # type: ignore
            return (None, claims)
