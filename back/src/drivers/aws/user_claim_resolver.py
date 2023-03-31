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
UserName = NewType("UserName", str)


@dataclass
class UserClaims:
    sub: UserSub
    username: UserName

    @staticmethod
    def from_response(response: GetUserResponseTypeDef) -> "UserClaims":
        sub = _get_sub(response["UserAttributes"])
        if sub == None:
            raise
        return UserClaims(
            UserSub(sub),
            UserName(response["Username"]),
        )


def _get_sub(attrs: List[AttributeTypeTypeDef]):
    sub: Optional[str] = None
    for attr in attrs:
        if attr["Name"] == "sub":
            sub = attr.get("Value")
    return sub


@inject
@dataclass
class UserClaimResolver:
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
