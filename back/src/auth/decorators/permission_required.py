from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from src.models import User
from typing import Tuple, Type


def permission_required(verifyed_models: Tuple[Type[User], ...]):
    def decorator(view_func):
        def _wrapped_view(self, request, *args, **kwargs):
            if isinstance(request.user, verifyed_models):
                return view_func(self, request, *args, **kwargs)
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        return _wrapped_view

    return decorator


login_required = permission_required((User))
