from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path

urlpatterns = [
    path("", lambda request: redirect("home")),
    path("admin/", admin.site.urls),
    path("auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),
]
