from django.shortcuts import render
from django.http import HttpResponse

from .models import Article
# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_details(request, article_id):
    article = Article.objects.all()[article_id]
    return render(request, 'articles/article_details.html', {'article': article})
    # return HttpResponse(f'You\'re looking at {article_id}.')