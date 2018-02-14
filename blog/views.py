import bleach
import markdown

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Article


# todo: move it away. make it tag?
def make_it_pretty(content: str) -> str:
    safe_content = bleach.clean(content)  # todo: remove html before storing it in db
    return markdown.markdown(safe_content, ouput_format='html5',
                             extensions=['markdown.extensions.extra'])


class Articles(ListView):

    http_method_names = ['get']
    template_name = 'blog/index.html'
    model = Article
    queryset = model.objects.all()[:4]
    context_object_name = 'articles'

    def get_context_data(self, **kwargs) -> dict:
        context = super(Articles, self).get_context_data(**kwargs)
        for article in context['articles']:
            article.content = make_it_pretty(article.content)
        return context

# class Article()

def article(request: WSGIRequest, article_id: int):
    article = Article.objects.get(id=article_id)
    make_it_pretty(article)
    return render(request, 'blog/single.html', context={'article': article})


def edit_test(request: WSGIRequest):
    return render(request, 'blog/post_editor.html')
