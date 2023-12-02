from django import forms
from core.models import *

class RecordForm(forms.ModelForm):
    success_url = 'contact'
    class Meta:
        model = record
        fields = ['name', 'number', 'email']