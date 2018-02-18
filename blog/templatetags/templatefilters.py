import markdown

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def markdown2html(content: str) -> str:
    return markdown.markdown(
        content, ouput_format='html5',
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.nl2br',  # cause newlines to be treated as hard breaks
            'blog.md_extensions.strikethrough'
        ]
    )
