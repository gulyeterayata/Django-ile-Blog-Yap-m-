from django.shortcuts import render

# Create your views here.


@login_required(login_url="user:login")
def pageadd(request):
    form = NewpageForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        newpage = form.save(commit = False)
        newpage.author = request.user
        newpage.save()
        return redirect("article:dashboard")
    son = Renk.objects.last()
    return render(request, "pageadd.html", {"form":form, "son":son,})
