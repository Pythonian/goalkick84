from django import forms
from .models import Article


class SearchForm(forms.Form):
    query = forms.CharField()

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['title', 'image', 'image_caption', 'excerpt',
				  'body', 'category', 'tags']