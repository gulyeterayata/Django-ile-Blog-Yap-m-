from django.db import models

# Create your models here.


class Anasayfa(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length = 50,verbose_name="Başlık Giriniz")
    alttitle = models.CharField(max_length = 50,verbose_name="Alt Başlık Giriniz")
    buton = models.CharField(max_length = 50,verbose_name="Buton için yönlendirme linki giriniz")
    
