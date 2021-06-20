from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.home,
        name="home"),

    url(r'^news/$',
        views.articles,
        name="articles"),

    url(r'^about/$',
        views.about,
        name="about"),

    url(r'^privacy/$',
        views.privacy,
        name="privacy"),

    url(r'^news/(?P<article_slug>[-\w]+)/$',
        views.article_detail,
        name="article_detail"),

    url(r'^news/(?P<article_slug>[-\w]+)/edit/$',
        views.edit,
        name="edit"),

    url(r'^category/(?P<category_slug>[-\w]+)/$',
        views.category,
        name="category"),

    url(r'^tag/(?P<tag_slug>[-\w]+)/$',
        views.tag_detail,
        name="tag_detail"),

    url(r'^search/$',
        views.search,
        name='search'),

    url(r'^new-post/$',
        views.new,
        name='new'),

]
