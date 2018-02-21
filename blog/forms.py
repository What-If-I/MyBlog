import bleach

from django.forms import ModelForm
from . import models


class Article(ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'content', 'published']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        form_data = super(Article, self).clean()
        content = form_data['content']
        # remove html before storing it in db
        safe_content = bleach.clean(content, tags=['br'])
        form_data['content'] = safe_content
        return form_data

    def save(self, commit=True):
        self.instance.author = self.user
        return super(Article, self).save(commit)
