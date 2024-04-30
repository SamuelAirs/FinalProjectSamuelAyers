from django.urls import path

from . import views

app_name = 'reminders'
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:reminders_id>/", views.reminder, name="reminder"),
    path("<int:reminders_id>/detail/", views.detail, name='detail')
]