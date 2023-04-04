from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from src.models import User
from typing import List


def login_required(view_func):
    def _wrapped_view(self, request, *args, **kwargs):
        if isinstance(request.user, User):
            return view_func(self, request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    return _wrapped_view


def permission_required(verifyed_models: List[User]):
    def decorator(view_func):
        def _wrapped_view(self, request, *args, **kwargs):
            if any([isinstance(request.user, user) for user in verifyed_models]):
                return view_func(self, request, *args, **kwargs)
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        return _wrapped_view

    return decorator
