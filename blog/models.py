from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        get_latest_by = 'updated_at'


class Article(TimeStampMixin, models.Model):
    """Blog article"""
    title = models.CharField(max_length=50, null=False)
    content = models.TextField()
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    published = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.title


class Comments(TimeStampMixin, models.Model):
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    message = models.TextField()

    def __str__(self):
        short_msg = self.message if len(self.message) < 21 else self.message[:20] + "..."
        return self.author + short_msg
