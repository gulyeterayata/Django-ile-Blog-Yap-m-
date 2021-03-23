from django.db import models
from ckeditor.fields import RichTextField
from sort_order_field import SortOrderField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 50,verbose_name="Kategori")
    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length = 50,verbose_name="Başlık")
    content = RichTextField()
    article_id = models.CharField(max_length=15, null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi")
    article_image= models.FileField(blank=True, null=True, verbose_name="Makaleye Fotoğraf Ekleyin.")
    category = models.CharField(max_length = 50, default = 'Yazılım Geliştirme')
    gorunum = models.CharField(max_length = 25, verbose_name = 'Görünürlük Belirleyin')
    sort = models.IntegerField(null=True)


    def __str__(self):
        return self.title

    





