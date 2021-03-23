from django import forms
from .models import Renk

class RenkForm(forms.ModelForm):
    class Meta:
        model = Renk
        fields = ["title"]