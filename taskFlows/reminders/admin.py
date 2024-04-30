from django.contrib import admin

from .models import reminderBase, reminderDetails

admin.site.register(reminderBase)
admin.site.register(reminderDetails)
