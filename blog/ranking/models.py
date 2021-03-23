from django.db import models

# Create your models here.

class Ranking(models.Model):
    rank = models.CharField(max_length = 50,verbose_name="Sıralama Belirleyiniz.")
    


