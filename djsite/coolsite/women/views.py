
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from .models import *

# Create your views here.
menu = ['о сайте', 'Добавить статью', 'Обратная связь', 'Войти']

def index(request):
    posts = Women.objects.all()
    return render(request,'women/index.html', {'posts': posts, 'menu':menu, 'title':'главная страница'}) 

def about(request):
    return render(request,'women/about.html', {'title':'о сайте'}) 

def categories(request, catid):
    if(request.GET):
        print(request.GET)
    
    return HttpResponse(f'<h1> Статьи по категориям</h1><p>{catid}</p>')

def categories_1(request, cat):
    return HttpResponse(f'<h1> Статьи по категориям cо slug</h1><p>{cat}</p>')

def archive(request, year):
    if int(year) <  2020:
        raise Http404()
    elif int(year) > 2030:
        #return redirect('/', permanent = True) #redirect 301- постоянный
        return redirect('home') # redirect 302-временный

    return HttpResponse(f'<h1> Архивы по годам cо slug</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

# в этих функциях не уверена в правильности аргументов тут написала общий принцип исключений
def pageNotFound_500(request):
    return HttpResponseNotFound('<h1>Ошибка сервера</h1>')

def pageNotFound_403(request, exception):
    return HttpResponseNotFound('<h1>доступ запрещен</h1>')

def pageNotFound_400(request, exception):
    return HttpResponseNotFound('<h1>невозможно обработать запрос</h1>')