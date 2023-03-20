from django.http.request import HttpRequest
from django.http.response import HttpResponse


def helth_check(request: HttpRequest):
    return HttpResponse("OK")
