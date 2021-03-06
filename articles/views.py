from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Article
# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'articles/article_details.html', {'article': article})

@login_required()
def article_create(request):
    return render(request, 'articles/article_create.html')