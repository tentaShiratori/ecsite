from django.urls import include, path

from . import CartList
from .reports import ReportList

urlpatterns = [
    path("", CartList.as_view()),
    path("reports/", ReportList.as_view()),
]
