from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Import the User model

class reminderBase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Creator")  # Add a foreign key to User
    reminderDescription = models.CharField(max_length=250)
    reminderCreationTime = models.DateTimeField("date published", auto_now_add=True)  # Automatically set the time when object is created
    reminderDetails = models.TextField(max_length=1000, default='')
    reminderDueDateStart = models.DateTimeField(null=True, blank=True)
    reminderDueDateEnd = models.DateTimeField(null=True, blank=True)
    reminderImportance = models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High'), (4, 'Critical')], default=1)
    reminderCompletion = models.BooleanField(default=False)

    def __str__(self):
        return self.reminderDescription

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.reminderCreationTime <= now




