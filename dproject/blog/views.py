from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


def create(request):
    if request.method == 'POST':  #-- - 1
        title = request.POST['title']  #-- - 2
        content = request.POST['content']  #-- - 2
        article = Article(title=title, content=content)  #-- - 3
        article.save()  #-- - 4
        return redirect('index')  #-- - 5
    else:
        params = {
            'form': ArticleForm(),
        }
        return render(request, 'blog/create.html', params)

def detail(request, article_id): #-- - 1
    article = Article.objects.get(id=article_id) #-- - 2
    params = {
        'article': article,
    }
    return render(request, 'blog/detail.html', params)

def index(request):
    articles = Article.objects.all()
    params = {
        'articles': articles,
    }
    return render(request, 'blog/index.html', params)