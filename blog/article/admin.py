from django.contrib import admin
from .models import Article, Category

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=["title","author","created_date", "article_id" ,"gorunum" , "sort"]
    search_fields=["title"]
    list_filter=["created_date"]
    class Meta:
        model = Article

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=["name", "id"]
    class Meta:
        model = Category











