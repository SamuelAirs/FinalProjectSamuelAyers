from django.urls import path

from . import views

app_name = 'reminders'
urlpatterns = [
    path("", views.index.as_view(), name="index"),
    path("<int:reminders_id>/", views.detail, name='detail'),
    path('new/', views.createReminder, name='createReminder'),
    path('toggle/<int:reminder_id>/', views.toggleCompletion, name='toggleCompletion'),
]