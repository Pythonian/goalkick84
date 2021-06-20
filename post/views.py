from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Q, Count
from .models import Article, Category, Tag
from .forms import SearchForm, ArticleForm
from django.utils.text import slugify
from django.db import models



def mk_paginator(request, items, num_items):
    '''Create and return a paginator.'''
    paginator = Paginator(items, num_items)
    try: page = int(request.GET.get('page', '1'))
    except ValueError: page = 1
    try: items = paginator.page(page)
    except (InvalidPage, EmptyPage):
        items = paginator.page(paginator.num_pages)
    return items


def home(request):
    section = "home"
    article_list = Article.objects.all()
    article_list = mk_paginator(request, article_list, 20)
    return render(
        request,
        'post/home.html',
        locals())


def articles(request):
    articles = Article.objects.all()
    articles = mk_paginator(request, articles, 8)
    return render(
        request,
        'post/articles.html',
        locals())


def article_detail(request, article_slug):
#    article = get_object_or_404(
#        Article, slug__iexact=article_slug)
    queryset = Article.objects.filter(
        slug__iexact=article_slug)
    if request:
        queryset.update(views=models.F("views") + 1)
    article = get_object_or_404(queryset)

    post_tags_ids = article.tags.values_list(
        'id', flat=True)
    similar_posts = Article.objects.filter(
        tags__in=post_tags_ids).exclude(id=article.id)
    similar_posts = similar_posts.annotate(
        same_tags=Count('tags')).order_by(
            '-same_tags', '-publish')[:4]
    return render(
        request,
        'post/post.html',
        locals())


def category(request, category_slug):
    category = get_object_or_404(
        Category, slug__iexact=category_slug)
    article_list = Article.objects.all().filter(category=category)
    article_list = mk_paginator(request, article_list, 20)
    return render(
        request,
        'post/category.html',
        locals())



def tag_detail(request, tag_slug):
    tag = get_object_or_404(
        Tag, slug__iexact=tag_slug)
    articles = Article.objects.all().filter(tags=tag)
    articles = mk_paginator(request, articles, 8)
    return render(
        request,
        'post/tag_detail.html',
        locals())


def search(request):
    form = SearchForm()
    articles = []
    if request.GET.has_key('query'):
        query = request.GET['query'].strip()
        if query:
            keywords = query.split()
            q = Q()
            for keyword in keywords:
                q = q & Q(title__icontains=keyword)
                form = SearchForm({'query': query})
                articles = Article.objects.filter(q)[:15]
    return render(
        request,
        'post/search.html',
        locals())


def about(request):
    section = "about"

    return render(
        request,
        'post/about.html',
        locals())


def privacy(request):
    section = "privacy"

    return render(
        request,
        'post/privacy.html',
        locals())


def new(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.slug = slugify(new_post.title)
        new_post.save()
        return HttpResponseRedirect(new_post.get_absolute_url())

    return render(
        request,
        'post/new.html',
        locals())

def edit(request, article_slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    post = get_object_or_404(
        Article,
        slug__iexact=article_slug)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(post.get_absolute_url())
    return render(
        request,
        "post/new.html",
        locals())
