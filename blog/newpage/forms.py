from django import forms
from sort_order_field import SortOrderField
from .models import Newpage, Pagecontent


choices = Newpage.objects.values_list()             # return ValuesQuerySet object
choices_list = []  # converts ValuesQuerySet into Python list
for item in choices:
    choices_list.append(item)

class NewpageForm(forms.ModelForm):
    class Meta:
        model = Newpage
        fields = ["page" ]



class PagecontentForm(forms.ModelForm):
    category = forms.ChoiceField(choices = choices_list)
    class Meta:
        model = Pagecontent
        fields = ["title", "content","article_image", "category"]
    
