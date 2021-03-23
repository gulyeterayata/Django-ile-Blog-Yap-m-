from django.db import models

# Create your models here.


class Onecikan(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE, verbose_name="Yazar")
    onecikanlar = models.CharField(max_length = 50,verbose_name="Anasayfa için öneçıkan İD'si belirleyin.")
    onecikanlar2 = models.CharField(max_length = 50 ,verbose_name="Anasayfa için öneçıkan İD'si belirleyin.")
    onecikanlar3 = models.CharField(max_length = 50 , verbose_name="Anasayfa için öneçıkan İD'si belirleyin.")


  

