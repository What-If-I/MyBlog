from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from . import models, forms


class Articles(ListView):

    http_method_names = ['get']
    template_name = 'blog/index.html'
    model = models.Article
    queryset = model.objects.filter(published=True).order_by('-id').all()[:4]
    context_object_name = 'articles'


class Article(DetailView):

    http_method_names = ['get']
    template_name = 'blog/single.html'
    model = models.Article
    pk_url_kwarg = 'article_id'
    context_object_name = 'article'


class ArticleCreate(CreateView):
    form_class = forms.Article
    template_name = 'blog/post_editor.html'

    def get_success_url(self):
        return reverse("article", args=(self.object.id, ))

    def get_form_kwargs(self):
        kwargs = super(ArticleCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
