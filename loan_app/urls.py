from django.urls import path, re_path
from loanapp.views import (
    CustomerView,
)

urlpatterns = [
    path("register-user/", CustomerView.as_view(), name="register_user"),
]

