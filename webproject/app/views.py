﻿"""
Definition of views.
"""

from datetime import datetime
from tokenize import Comment
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import FeedbackForm, CommentForm, BlogForm
from django.contrib.auth.forms import UserCreationForm


from django.db import models;
from .models import Blog, Comment



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Страница с нашими контактами.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'message':'Сведения о нас.',
            'year':datetime.now().year,
        }
    )

def links(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            'title':'Полезные ссылки',
            'year':datetime.now().year,
        }
    )


def feedback(request):
    assert isinstance(request, HttpRequest)
    feedback = None
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.cleaned_data
            form = None
    else:
        form = FeedbackForm()
    return render(
        request,
        'app/pool.html',
        {
            'title':'Обратная связь',
            'form': form, 
            'feedback': feedback,
        }
    )

def registration(request):
    assert isinstance(request, HttpRequest)

    if request.method == "POST": # после отправки формы

        regform = UserCreationForm (request.POST)

        if regform.is_valid(): #валидация полей формы

            reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы

            reg_f.is_staff = False # запрещен вход в административный раздел

            reg_f.is_active = True # активный пользователь

            reg_f.is_superuser = False # не является суперпользователем

            reg_f.date_joined = datetime.now() # дата регистрации

            reg_f.last_login = datetime.now() # дата последней авторизации

            reg_f.save() # сохраняем изменения после добавления данных

            return redirect('home') # переадресация на главную страницу после регистрации
    else:

        regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя
# создание объекта формы для ввода данных нового пользователя

    return render(

        request,

        'app/registration.html',

        {

            'regform': regform, # передача формы в шаблон веб-страницы

            'year':datetime.now().year,

        }

)

def blog(request):

    assert isinstance(request, HttpRequest)

    posts = Blog.objects.all()

    return render(

        request,

        'app/blog.html',

        {

            'title':'Блог',

            'posts': posts, 

            'year':datetime.now().year,

        }

)

def blogpost(request, parametr):
    assert isinstance(request, HttpRequest)
    post_1 = Blog.objects.get(id=parametr)
    comments = Comment.objects.filter(post = parametr)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = Blog.objects.get(id = parametr)
            comment_f.save()
            return redirect('blogpost', parametr = post_1.id)
    else: 
        form = CommentForm()

    return render(
        request,
            'app/blogpost.html',
            {
                'post_1': post_1,
                'comments': comments,
                'form': form,
                'year':datetime.now().year,
            }
                
        )

def newpost(request):
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.author = request.user
            blog_f.save()

            return redirect('blog')
    else:
        blogform = BlogForm()

    return render(
        request,
        'app/newpost.html',
        {
            'blogform': blogform,
            'title': 'Добавить статью блога',
            'year': datetime.now().year,
         }
        )

def videopost(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title':'Видео',
            'year':datetime.now().year,
        }
    )


            
            
