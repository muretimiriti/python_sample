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


def index(request):
    articles = Article.objects.all()
    params = {
        'articles': articles,
    }
    return render(request, 'blog/index.html', params)