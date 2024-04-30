from django.urls import path

from . import views

app_name = 'reminders'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:reminders_id>/", views.detail, name='detail')
]