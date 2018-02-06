from django.shortcuts import render
from .models import Article
import bleach
import markdown


# todo: move it away. make it tag?
def make_it_pretty(article: Article) -> Article:
    safe_content = bleach.clean(article.content)  # todo: remove html before storing it in db
    article.content = markdown.markdown(safe_content, ouput_format='html5', extensions=['markdown.extensions.extra'])
    return article


def index(request):
    articles = Article.objects.all()[:4]
    context = {
        'articles': articles,
    }
    for article in articles:
        make_it_pretty(article)
    return render(request, 'blog/index.html', context)


def article(request, article_id):
    article = Article.objects.get(id=article_id)
    make_it_pretty(article)
    return render(request, 'blog/single.html', context={'article': article})
