from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('',
         views.home,
         name="home"),

    path('news/',
         views.articles,
         name="articles"),

    path('about/',
         views.about,
         name="about"),

    path('privacy/',
         views.privacy,
         name="privacy"),

    path('news/<slug:article_slug>/',
         views.article_detail,
         name="article_detail"),

    path('news/<slug:article_slug>/edit/',
         views.edit,
         name="edit"),

    path('category/<slug:category_slug>/',
         views.category,
         name="category"),

    path('tag/<slug:tag_slug>/',
         views.tag_detail,
         name="tag_detail"),

    path('search/',
         views.search,
         name='search'),

    path('new-post/',
         views.new,
         name='new'),

]
