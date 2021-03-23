from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .forms import RenkForm
from .models import Renk
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def colorchange(request):
    form = RenkForm(request.POST or None)

    if form.is_valid():
        renk = form.save(commit = False)
        renk.author = request.user
        renk.save()
        messages.success(request,"Renk başarıyla değişti!")
        return redirect("article:dashboard")
    return render(request, "colorchange.html", {"form" : form})
