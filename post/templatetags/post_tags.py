from django import template

from ..models import Article

register = template.Library()


@register.inclusion_tag('post/latest_posts.html')
def get_latest_articles():
    return {'latest_articles': Article.objects.all()[:3]}


def latest_articles():
    return {'latest_articles': Article.objects.all()[:3]}
