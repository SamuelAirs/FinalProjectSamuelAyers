from django import forms
from .models import reminderBase

class reminderForm(forms.ModelForm):
    class Meta:
        model = reminderBase
        fields = ['reminderDescription', 'reminderDetails', 'reminderDueDateStart', 'reminderDueDateEnd', 'reminderImportance']
        labels = {
            'reminderDescription': 'Description',
            'reminderDetails': 'Details',
            'reminderDueDateStart': 'Start Date',
            'reminderDueDateEnd': 'Due Date',
            'reminderImportance': 'Importance',
        }
        widgets = {
            'reminderDueDateStart': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'reminderDueDateEnd': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }
