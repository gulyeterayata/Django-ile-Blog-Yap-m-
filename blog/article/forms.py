from django import forms
from .models import Article, Category
from renk.models import Renk
from onecikan.models import Onecikan
from anasayfa.models import Anasayfa



choices = Category.objects.all().values_list('name' , 'name')
choices_list = []
for item in choices:
    choices_list.append(item)

CHOICES = (
        (0, 'Gizle'),
        (1, 'Göster'),
    )


class ArticleForm(forms.ModelForm):
    category = forms.ChoiceField(choices = choices_list)
    gorunum = forms.ChoiceField(choices = CHOICES)
    class Meta:
        model = Article
        fields = ["title", "content","article_image", "article_id", "category", "gorunum" , "sort"]
        
        
class RenkForm(forms.ModelForm):
    class Meta:
        model = Renk
        fields = ["title" ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]



class OnecikanForm(forms.ModelForm):
    class Meta:
        model = Onecikan
        fields = ["onecikanlar", "onecikanlar2", "onecikanlar3" ]


class AnasayfaForm(forms.ModelForm):
    class Meta:
        model = Anasayfa
        fields = ["title", "alttitle","buton",]


