from django.shortcuts import render
from django.http import HttpResponse

def  index(request):
    return HttpResponse('<h1>Главная</h1>')

def about(request):
    return HttpResponse('<h2>Обо мне</h2>')


