# account/forms.py
from django import forms
from .models import Task

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['completed', 'note']
