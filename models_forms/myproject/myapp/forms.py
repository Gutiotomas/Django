from django import forms

SHIFTS= (
    ("1", "Morning"),
    ("2", "Afternoon"),
    ("3", "Night"),
)

class InputForm(forms.Form):
    first_name= forms.CharField(max_length=200, required = False)
    last_name = forms.CharField(max_length=200)
    shift = forms.ChoiceField(choices = SHIFTS)    
    time_log = forms.TimeField(help_text= "Enter the exact time")