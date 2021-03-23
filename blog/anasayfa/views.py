from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from anasayfa.models import Anasayfa
from anasayfa.forms import AnasayfaForm
from renk.forms import RenkForm
from renk.models import Renk
from article.forms import OnecikanForm
from article.forms import CategoryForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required(login_url="user:login")
def addAnasayfa(request):
    form = AnasayfaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        anasayfa = form.save(commit = False)
        anasayfa.author = request.user
        anasayfa.save()
        messages.success(request, "Değişiklikler kaydedildi.")
        return redirect("article:dashboard")
        
    son = Renk.objects.last()
    categorys = Category.objects.all()
    return render(request, "anasayfaedit.html", {"form":form, "son":son, "categorys":categorys})
