from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Главная страница
def index(request):    
    return HttpResponse('Главная страница')

# Лента постов групп
def group_posts(request, pk):
    return HttpResponse(f'Группа id {pk}')
