from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from src.models import User


def login_required(view_func):
    def _wrapped_view(self, request, *args, **kwargs):
        print(request.user)
        if isinstance(request.user, User):
            return view_func(self, request, *args, **kwargs)
        return Response(status=status.HTTP_404_NOT_FOUND)

    return _wrapped_view
