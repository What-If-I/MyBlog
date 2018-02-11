import bleach
import markdown

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from .models import Article


# todo: move it away. make it tag?
def make_it_pretty(article: Article) -> Article:
    safe_content = bleach.clean(article.content)  # todo: remove html before storing it in db
    article.content = markdown.markdown(safe_content, ouput_format='html5', extensions=['markdown.extensions.extra'])
    return article


def index(request: WSGIRequest):
    articles = Article.objects.all()[:4]
    context = {
        'articles': articles,
    }
    for article in articles:
        make_it_pretty(article)
    return render(request, 'blog/index.html', context)


def article(request: WSGIRequest, article_id: int):
    article = Article.objects.get(id=article_id)
    make_it_pretty(article)
    return render(request, 'blog/single.html', context={'article': article})


def edit_test(request: WSGIRequest):
    return render(request, 'blog/post_editor.html')
