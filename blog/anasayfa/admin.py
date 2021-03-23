from django.contrib import admin
from .models import Anasayfa

# Register your models here.

@admin.register(Anasayfa)
class AnasayfaAdmin(admin.ModelAdmin):
    list_display=["author","title","alttitle", "buton"]
    class Meta:
        model = Anasayfa
