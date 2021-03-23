from django.db import models

# Create your models here.
 
class Renk(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length = 50,verbose_name="Renk Adı:")

    
    

