from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .forms import ArticleForm
from .models import Article, Category
from anasayfa.models import Anasayfa
from anasayfa.forms import AnasayfaForm
from newpage.models import Newpage
from newpage.forms import NewpageForm
from newpage.models import Pagecontent
from newpage.forms import PagecontentForm
from renk.forms import RenkForm
from renk.models import Renk
from .forms import OnecikanForm
from .forms import CategoryForm
from onecikan.models import Onecikan
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def articles(request):
    articles = Article.objects.filter(gorunum = "1").order_by("sort")
    son = Renk.objects.last()
    categorys = Category.objects.all()
    newpages = Newpage.objects.all()
    return render(request, "articles.html", {"articles":articles, "newpages":newpages, "son":son, "categorys":categorys, })



def index(request):
    articles = Article.objects.all()
    random = Article.objects.last()
    son = Renk.objects.last()
    last = Onecikan.objects.last()
    categorys = Category.objects.all()
    newpages = Newpage.objects.all()
    id1 = last.onecikanlar
    id2 = last.onecikanlar2
    id3 = last.onecikanlar3
    lookedforarticle = Article.objects.get(article_id = id1)
    lookedforarticle2 = Article.objects.get(article_id = id2)
    lookedforarticle3 = Article.objects.get(article_id = id3)
    edit = Anasayfa.objects.last()
    
    return render(request, "index.html",  {"articles":articles, "newpages":newpages, "edit":edit, "random":random , "son":son, "last":lookedforarticle, "lookedforarticle3":lookedforarticle3, "lookedforarticle2":lookedforarticle2, "categorys":categorys })


def onecikan(request):
    form = OnecikanForm(request.POST or None)
    print('here')
    if form.is_valid():
        onecikan = form.save(commit = False)
        onecikan.author = request.user
        onecikan.save()
        messages.success(request,"Renk başarıyla değişti!")
        return redirect("article:dashboard")
    categorys = Category.objects.all()
    son = Renk.objects.last()
    newpages = Newpage.objects.all()
    return render(request, "onecikan.html", {"form" : form, "newpages":newpages, "son":son, "categorys":categorys})

def about(request):
    son = Renk.objects.last()
    categorys = Category.objects.all()
    newpages = Newpage.objects.all()
    return render(request, "about.html", {"son":son, "newpages":newpages, "categorys":categorys})

def dashboard(request):
    son = Renk.objects.last()
    articles = Article.objects.filter(author = request.user)
    categorys = Category.objects.all()
    newpages = Newpage.objects.all()
    context={
        "articles":articles,
        "son":son,
        "categorys":categorys,
        "newpages":newpages,
    }
    return render(request, "dashboard.html", context)

@login_required(login_url="user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale başarıyla oluşturuldu.")
        return redirect("article:dashboard")
        
    son = Renk.objects.last()
    categorys = Category.objects.all()
    newpages = Newpage.objects.all()
    return render(request, "addarticle.html", {"form":form, "son":son, "newpages":newpages, "categorys":categorys})

@login_required(login_url="user:login")
def addContent(request):
    form = PagecontentForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article2 = form.save(commit = False)
        article2.author = request.user
        article2.save()
        messages.success(request, "Makale başarıyla oluşturuldu.")
        return redirect("article:dashboard")
        
    son = Renk.objects.last()
    categorys = Category.objects.all()
    newpages = Newpage.objects.all()
    return render(request, "pageadd.html", {"form":form, "son":son, "newpages":newpages, "categorys":categorys})




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
    newpages = Newpage.objects.all()
    return render(request, "anasayfaedit.html", {"form":form, "son":son, "newpages":newpages, "categorys":categorys})


@login_required(login_url="user:login")
def categoryadd(request):
    form = CategoryForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        category = form.save(commit = False)
        category.author = request.user
        category.save()
        return redirect("article:categoryadd")
    son = Renk.objects.last()
    categorys = Category.objects.all()
    newpages = Newpage.objects.all()
    return render(request, "categoryadd.html", {"form":form, "newpages":newpages, "son":son, "categorys":categorys})


def colorchange(request):

    form = RenkForm(request.POST or None)
    print('here')
    if form.is_valid():
        renk = form.save(commit = False)
        renk.author = request.user
        renk.save()
        messages.success(request,"Renk başarıyla değişti!")
        return redirect("article:dashboard")
    son = Renk.objects.last()
    categorys = Category.objects.all()
    newpages = Newpage.objects.all()
    return render(request, "colorchange.html", {"form" : form, "newpages":newpages, "son":son, "categorys":categorys})

def detail(request, article_id, category):
    article = get_object_or_404(Article, article_id = article_id, category=category)
    son = Renk.objects.last()
    categorys = Category.objects.all()
    newpages = Newpage.objects.all()
    return render(request, "detail.html",{"article":article, "newpages":newpages, "son":son, "categorys":categorys})


def detail(request, article_id, category):
    article = get_object_or_404(Article, article_id = article_id, category=category)
    son = Renk.objects.last()
    categorys = Category.objects.all()
    newpages = Newpage.objects.all()
    return render(request, "detail.html",{"article":article, "newpages":newpages, "son":son, "categorys":categorys})





@login_required(login_url="user:login")
def update(request, article_id, category):
    article = get_object_or_404(Article, article_id = article_id, category=category)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale başarıyla güncellendi.")
        return redirect("article:dashboard")
    son = Renk.objects.last()
    categorys = Category.objects.all()
    newpages = Newpage.objects.all()
    return render(request,"update.html", {"form":form, "newpages":newpages, "son":son, "categorys":categorys})



@login_required(login_url="user:login")
def deleteArticle(request, article_id, category):
    article = get_object_or_404(Article, article_id = article_id, category=category)
    article.delete()
    messages.success(request,"Makale başarıyla silindi.")
    
    return redirect("article:dashboard")



@login_required(login_url="user:login")
def deleteCategory(request, id):
    category = get_object_or_404(Category, id = id)
    category.delete()
    messages.success(request,"Silindi.")
    
    return redirect("article:categoryadd")




def categorydetail(request, id):
    cat1 = get_object_or_404(Category, id = id)
    articles = Article.objects.filter(category = cat1 , gorunum = "1").order_by("-created_date")
    son = Renk.objects.last()
    categorys = Category.objects.all()
    newpages = Newpage.objects.all()
    return render(request, "categorydetail.html",{"articles":articles, "newpages":newpages, "son":son, "categorys":categorys})



def newpagedetail(request, id):
    articles = Pagecontent.objects.filter(category = id).order_by("-created_date")
    son = Renk.objects.last()
    categorys = Category.objects.all()
    newpages = Newpage.objects.all()
    return render(request, "newpagedetail.html",{"articles":articles, "newpages":newpages ,"son":son, "categorys":categorys})


@login_required(login_url="user:login")
def deleteNewpage(request, id):
    newpage = get_object_or_404(Newpage, id = id)
    newpage.delete()
    messages.success(request,"Silindi.")

    return redirect("article:dashboard")




@login_required(login_url="user:login")
def pageadd(request):
    form = NewpageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        newpage = form.save(commit = False)
        newpage.author = request.user
        newpage.save()
        return redirect("article:dashboard")
        
    newpages = Newpage.objects.all()
    son = Renk.objects.last()
    newpages = Newpage.objects.all()
    return render(request, "pageadd.html", {"form":form, "newpages":newpages, "son":son, "newpages":newpages})


@login_required(login_url="user:login")
def addContent(request):
    form = PagecontentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        content = form.save(commit = False)
        content.author = request.user
        content.save()
        messages.success(request, "Makale başarıyla oluşturuldu.")
        return redirect("article:pageadd")
        
    son = Renk.objects.last()
    categorys = Category.objects.all()
    newpages = Newpage.objects.all()
    return render(request, "content.html", {"form":form, "newpages":newpages, "son":son, "categorys":categorys})



    







