from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from article.forms import CategoryForm
from article.models import Category
from newpage.forms import NewpageForm
from newpage.models import Newpage
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from renk.forms import RenkForm
from renk.models import Renk




# Create your views here.

def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username =username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.info(request,"Başarıyla Kayıt Oldunuz...")
        return redirect("index")
    son = Renk.objects.last()
    categorys = Category.objects.all()
    newpages = Newpage.objects.all()
    context = {
            "form" : form,
            "son" : son,
            "categorys":categorys,
            "newpages":newpages,
        }
    return render(request,"register.html",context)

    
    
def loginUser(request):
    form = LoginForm(request.POST or None)
    son = Renk.objects.last()
    categorys = Category.objects.all()
    newpages = Newpage.objects.all()
    context = {
        "form":form,
        "son": son,
        "categorys":categorys,
        "newpages":newpages,
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",context)
        
        messages.success(request,"Başarıyla Giriş Yaptınız")
        login(request,user)
        return redirect("/articles/dashboard/")
    
    return render(request,"login.html",context)
def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")