from django.contrib import admin
from .models import Renk

# Register your models here.

@admin.register(Renk)


class RenkAdmin(admin.ModelAdmin):
    list_display=["title","author"]

    class Meta:
        model = Renk