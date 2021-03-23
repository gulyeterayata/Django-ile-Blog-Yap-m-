from django.contrib import admin
from django.urls import path
from . import views
app_name = "anasayfa"

urlpatterns = [
    path('anasayfaedit/', views.addAnasayfa, name="anasayfaedit"),

]

