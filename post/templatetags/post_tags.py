from django import template

register = template.Library()

from ..models import Article

@register.assignment_tag
def get_latest_articles():
    return Article.objects.all()[:3]
