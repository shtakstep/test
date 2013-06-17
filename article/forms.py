from django import forms
from article.models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'body', 'pub_date', 'thumbnail')


class CommentForms(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'body')
