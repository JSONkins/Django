from datetime import datetime

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ArticleForm
from .models import Article


def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Article not found")

    latest_comments_list = a.comment_set.order_by('-id')[:5]

    return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Article not found")
    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))


def create(request):

    if request.method == 'POST':
        a = Article(article_title=request.POST['Title'], article_text=request.POST['Text'], pub_date=datetime.now())
        a.save()
        return HttpResponseRedirect(reverse('articles:index'))

    return render(request, 'articles/create.html')
