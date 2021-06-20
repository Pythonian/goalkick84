from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(
        max_length=50)
    slug = models.SlugField(
        max_length=50,
        unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'post:category',
            args=[self.slug])


class Tag(models.Model):
    title = models.CharField(
        max_length=50)
    slug = models.SlugField(
        max_length=50,
        unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'post:tag',
            args=[self.slug])


class Article(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True)
    slug = models.SlugField(
        max_length=100,
        help_text="Builds the Article's URL from the title.")
    image = models.ImageField(
        upload_to="images")
    image_caption = models.CharField(
        max_length=100,
        blank=True,
        help_text="(Optional) Image's caption.")
    excerpt = models.TextField()
    body = RichTextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True)
    tags = models.ManyToManyField(
        Tag,
        blank=True)
    publish = models.DateTimeField(
        "Published on",
        auto_now_add=True)
    guest_author = models.CharField(
        help_text='If the Author is not a registered user, type the name here.',
        max_length=50,
        blank=True,
        null=True)
    is_published = models.BooleanField(
        default=True,
        help_text="Uncheck this if you don't want the article to appear on the site yet.")
    featured = models.BooleanField(
        default=False)
    views = models.PositiveIntegerField(
        default=0,
        editable=False)

    class Meta:
        ordering = ['-publish']
        get_latest_by = 'publish'

    def __str__(self):
        return self.title

    def get_previous_post(self):
        return self.get_previous_by_publish()

    def get_next_post(self):
        return self.get_next_by_publish()

    def get_absolute_url(self):
        return reverse(
            'post:article_detail',
            args=[self.slug])

    def get_edit_url(self):
        return reverse(
            'post:edit',
            args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        self.guest_author = ""

        super().save(*args, **kwargs)
