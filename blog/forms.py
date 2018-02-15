from django.forms import ModelForm
from . import models


class Article(ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'content', 'published']
