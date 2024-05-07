from django.urls import path

from . import views
from .views import send_reminder_email

app_name = 'reminders'
urlpatterns = [
    path("", views.index.as_view(), name="index"),
    path('send_email/', send_reminder_email, name='send_reminder_email'),
    path("<int:reminders_id>/", views.detail, name='detail'),
    path('new/', views.createReminder, name='createReminder'),
    path('toggle/<int:reminder_id>/', views.toggleCompletion, name='toggleCompletion'),
    path('edit/<int:reminder_id>/', views.editReminder, name='editReminder'),
    path('complete/', views.completedReminders.as_view(), name='completedReminders'),
    path('reminders/delete/<int:reminder_id>/', views.deleteReminder, name='deleteReminder'),
]