from django.contrib import admin
from .models import Ranking

# Register your models here.
@admin.register(Ranking)
class RankingAdmin(admin.ModelAdmin):
    list_display=["rank", "id"]
    class Meta:
        model = Ranking