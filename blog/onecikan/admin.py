from django.contrib import admin
from .models import Onecikan


# Register your models here.

@admin.register(Onecikan)


class OnecikanAdmin(admin.ModelAdmin):
    list_display=["author", "onecikanlar", "onecikanlar2", "onecikanlar3"]

    class Meta:
        model = Onecikan