from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    
    context = {
        'articles' : articles
    }

    return render(request, 'movies/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article' : article
    }

    return render(request, 'movies/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('movies:detail', article.pk)
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'movies/create.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('movies:index')
    else:
        redirect('movies:detail', article.pk)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {'form': form, 'article': article}
    return render(request, 'movies/update.html', context)