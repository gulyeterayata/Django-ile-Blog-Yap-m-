from django.contrib import admin
from django.urls import path
from . import views
app_name = "onecikan"

urlpatterns = [
    path('onecikan/', views.onecikan, name="onecikan"),

]

