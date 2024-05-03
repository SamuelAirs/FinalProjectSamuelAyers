from django import forms
from .models import reminderBase

class reminderForm(forms.ModelForm):
    class Meta:
        model = reminderBase
        fields = ['reminderDescription', 'reminderDetails', 'reminderDueDateStart', 'reminderDueDateEnd', 'reminderImportance']
        widgets = {
            'reminderDueDateStart': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'reminderDueDateEnd': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
