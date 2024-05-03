from django import forms
from .models import reminderBase

class reminderForm(forms.ModelForm):
    class Meta:
        model = reminderBase
        fields = ['reminderDescription', 'reminderCreationTime', 'reminderDetails', 'reminderDueDateStart', 'reminderDueDateEnd', 'reminderImportance', 'reminderCompletion']
        widgets = {
            'reminderCreationTime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'reminderDueDateStart': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'reminderDueDateEnd': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
