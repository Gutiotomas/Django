from django import forms
from .models import Logger

class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = ["first_name", "last_name", "time_log"]