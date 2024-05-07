
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("reminders/", include("reminders.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]
