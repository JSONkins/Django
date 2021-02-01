from django.forms import ModelForm, TextInput, Textarea, DateField

from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["article_title", "article_text",]
        widgets = {
            "article_title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title here'
            }),
            "article_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text here'
            })
        }
