from django.shortcuts import render
from .models import Article #-- - 1


def index(request):
    articles = Article.objects.all() #-- - 2
    params = {
        'articles': articles,  #-- - 3
    }
    return render(request, 'blog/index.html', params) #-- - 4