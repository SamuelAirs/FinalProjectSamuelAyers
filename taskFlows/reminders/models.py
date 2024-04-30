import datetime

from django.db import models
from django.utils import timezone

class reminderBase(models.Model):
    reminderDescription = models.CharField(max_length=250)
    reminderCreationTime = models.DateTimeField("date published")
    def __str__(self):
        return self.reminderDescription

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class reminderDetails(models.Model):
    reminder = models.ForeignKey(reminderBase, on_delete=models.CASCADE)
    reminderDetails = models.TextField(max_length=1000, default='')
    reminderDueDateStart = models.DateTimeField()
    reminderDueDateEnd = models.DateTimeField()
    reminderImportance = models.IntegerChoices('1', '2', '3', '4')
    reminderCompletion = models.IntegerChoices('0', '1')
    def __str__(self):
        return self.reminderDetails


