from django.contrib import admin
from django.urls import path
from . import views
app_name = "article"

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addarticle/', views.addArticle, name="addarticle"),
    path('categoryadd/', views.categoryadd, name="categoryadd"),
    path('pageadd/', views.pageadd, name="pageadd"),
    path('colorchange/', views.colorchange, name="colorchange"),
    path('anasayfaedit/', views.addAnasayfa, name="anasayfaedit"),
    path('article/<str:category>/<str:article_id>',views.detail,name = "detail"),
    path('article/<int:id>',views.categorydetail,name = "categorydetail"),
    path('newpagedetail/<int:id>',views.newpagedetail,name = "newpagedetail"),

    path('update/<str:category>/<str:article_id>',views.update,name = "update"),
    path('delete/<str:category>/<str:article_id>',views.deleteArticle,name = "delete"),
    path('delete/<int:id>',views.deleteCategory,name = "deleteCategory"),
    path('deletepage/<int:id>',views.deleteNewpage,name = "deleteNewpage"),
    path('contentadd/',views.addContent,name = "addContent"),
    path('',views.articles,name = "articles"),
]

