from ckeditor.fields import RichTextField
from sort_order_field import SortOrderField
from django.db import models


# Create your models here.

class Newpage(models.Model):
    page = models.CharField(max_length = 50,verbose_name="Yeni Sayfa Oluşturunuz.")
    def __str__(self):
        return self.page


class Pagecontent(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length = 50,verbose_name="Başlık")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi")
    article_image= models.FileField(blank=True, null=True, verbose_name="Yazınıza Fotoğraf Ekleyin.")
    category = models.CharField(max_length = 50, default = '-')

    def __str__(self):
        return self.title





    


    


