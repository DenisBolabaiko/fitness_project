"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Ваше имя', required=True)
    city = forms.CharField(label='Город', required=True)
    email = forms.CharField(label='Почта', required=True)
    rating = forms.ChoiceField(
        choices=[(1, '1 - Плохо'), (2, '2 - Удовлетворительно'), (3, '3 - Нормально'), (4, '4 - Хорошо'), (5, '5 - Отлично')],
        label='Оценка сайта',
        required=True
    )
    comments = forms.CharField(widget=forms.Textarea, label='Ваши пожелания', required=False)
    recommend = forms.BooleanField(label='Рекомендуете ли вы наш сайт?', required=False)
    feature_request = forms.CharField(label='Что бы вы хотели улучшить?', required=False)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Комментарий"}

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description':"Краткое описание", 'content': "Полное содержание", 'image': "Картинка"}