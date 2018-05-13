from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from articles.models import Article
from . import forms


def article_list(request):
    articles = Article.objects.all().order_by('date')

    context = {
        'articles': articles
    }

    return render(request, 'articles/article_list.html', context)


def article_details(request, slug):
    article = Article.objects.get(slug=slug)
    context = {
        'article': article
    }
    return render(request, 'articles/article_details.html', context)


@login_required(login_url='/accounts/login/')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle
    context = {
        'form': form
    }
    return render(request, 'articles/article_create.html', context)
