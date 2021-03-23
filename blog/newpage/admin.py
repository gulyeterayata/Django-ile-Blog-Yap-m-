from django.contrib import admin
from .models import Newpage, Pagecontent

# Register your models here.

@admin.register(Newpage)
class NewpageAdmin(admin.ModelAdmin):
    list_display=["page" , "id"]
    class Meta:
        model = Newpage


@admin.register(Pagecontent)
class PagecontentAdmin(admin.ModelAdmin):
    list_display=["author","title","content","article_image","category"]
    class Meta:
        model = Pagecontent
