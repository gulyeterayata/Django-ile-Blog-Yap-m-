from django import forms
from .models import Anasayfa





class AnasayfaForm(forms.ModelForm):
    class Meta:
        model = Anasayfa
        fields = ["title", "alttitle","buton",]