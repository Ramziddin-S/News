from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Category,News,Author,Reference
from .forms import CategoryForm,NewsForm,AuthorForm,ReferenceForm

def login_required_decorator(f):
    return login_required(f, login_url="login")


@login_required_decorator
def dashboard_page(request):
    return render(request, 'dashboard/index.html')


def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')


def dashboard_logout(request):
    logout(request)
    return redirect('login')


def category_list(request):
    categories = Category.objects.all()
    ctx = {
        "categories": categories
    }
    return render(request, 'dashboard/category/list.html', ctx)


def category_create(request):
    model = Category()
    form = CategoryForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/category/form.html',ctx)


def news_list(request):
    news = News.objects.all()
    ctx = {
        "news": news
    }
    return render(request, 'dashboard/news/list.html', ctx)


def news_create(request):
    model = News()
    form = NewsForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('news_list')
        else:
            print(form.errors)
    ctx = {
    "form": form
                 }
    return render(request, 'dashboard/news/form.html',ctx)



def news_edit(request):
    model = News()
    form = NewsForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('news_list')
        else:
            print(form.errors)
    ctx = {
    "form": form
                 }
    return render(request, 'dashboard/news/form.html',ctx)

def delete_news(request, news_id):
    model = News.objects.get(id=news_id)
    model.delete()
    return redirect("news_list")



def authors_list(request):
    authors = Author.objects.all()
    ctx = {
        "authors": authors
    }
    return render(request, 'dashboard/author/list.html', ctx)


def authors_create(request):
    model = Author()
    form = AuthorForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('authors_list')
        else:
            print(form.errors)
    ctx = {
    "form": form
                 }
    return render(request, 'dashboard/author/form.html',ctx)


def references_list(request):
    references = Reference.objects.all()
    ctx = {
        "references": references
    }
    return render(request, 'dashboard/reference/list.html', ctx)


def references_create(request):
    model = Reference()
    form = ReferenceForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('references_list')
        else:
            print(form.errors)
    ctx = {
    "form": form
                 }
    return render(request, 'dashboard/reference/form.html',ctx)


