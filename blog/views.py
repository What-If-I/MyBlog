import bleach
import markdown

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView


from . import models, forms


# todo: move it away. make it tag?
def make_it_pretty(content: str) -> str:
    safe_content = bleach.clean(content)  # todo: remove html before storing it in db
    return markdown.markdown(safe_content, ouput_format='html5',
                             extensions=['markdown.extensions.extra'])


class Articles(ListView):

    http_method_names = ['get']
    template_name = 'blog/index.html'
    model = models.Article
    queryset = model.objects.all()[:4]
    context_object_name = 'articles'

    def get_context_data(self, **kwargs) -> dict:
        context = super(Articles, self).get_context_data(**kwargs)
        for article in context['articles']:
            article.content = make_it_pretty(article.content)
        return context


class Article(DetailView):

    http_method_names = ['get']
    template_name = 'blog/single.html'
    model = models.Article
    pk_url_kwarg = 'article_id'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(Article, self).get_context_data(**kwargs)
        context['article'].content = make_it_pretty(context['article'].content)
        return context


class ArticleEdit(CreateView):
    form_class = forms.Article
    template_name = 'blog/post_editor.html'
