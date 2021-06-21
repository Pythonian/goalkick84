from django import template

from ..models import Article

register = template.Library()


@register.inclusion_tag('post/latest_posts.html')
def get_latest_articles(count=4):
    return {'latest_articles': Article.objects.all()[:count]}
