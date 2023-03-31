from mypy_boto3_cognito_idp import CognitoIdentityProviderClient
from injector import inject
import boto3
from mypy_boto3_cognito_idp.type_defs import (
    GetUserResponseTypeDef,
    AttributeTypeTypeDef,
)
from botocore.exceptions import ClientError
from dataclasses import dataclass
from typing import NewType, List, Optional

UserSub = NewType("UserSub", str)
UserEmail = NewType("UserEmail", str)


@dataclass
class UserClaims:
    sub: UserSub
    email: UserEmail

    @staticmethod
    def from_response(response: GetUserResponseTypeDef) -> "UserClaims":
        email = _get_email(response["UserAttributes"])
        if email is None:
            raise
        return UserClaims(
            UserSub(response["Username"]),
            UserEmail(email),
        )


def _get_email(attrs: List[AttributeTypeTypeDef]):
    sub: Optional[str] = None
    for attr in attrs:
        if attr["Name"] == "email":
            sub = attr.get("Value")
    return sub


@inject
@dataclass
class UserClaimsResolver:
    client: CognitoIdentityProviderClient

    def run(self, token: str) -> Optional[UserClaims]:
        try:
            response = self.client.get_user(AccessToken=token)
            return UserClaims.from_response(response)
        except ClientError as e:
            if (
                e.response.get("Error", {}).get("Code", "Unknown")
                == "NotAuthorizedException"
            ):
                return None
            raise e
