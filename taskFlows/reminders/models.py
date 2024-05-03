from django.db import models
from django.utils import timezone

class reminderBase(models.Model):
    reminderDescription = models.CharField(max_length=250)
    reminderCreationTime = models.DateTimeField("date published")
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



