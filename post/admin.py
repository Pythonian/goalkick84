from django.contrib import admin
from .models import Category, Tag, Article


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'slug']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
    list_filter = ['publish']
    list_display = ['title', 'category', 'publish', 'views']
from django.contrib import admin
from .models import Category, Tag, Article


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'slug']
admin.site.unregister(Category)
admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.unregister(Tag)
admin.site.register(Tag, TagAdmin)


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
    list_filter = ['publish']
    list_display = ['title', 'category', 'publish', 'views']
admin.site.unregister(Article)
admin.site.register(Article, ArticleAdmin)

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('title',)}
#     list_display = ['title', 'slug']
