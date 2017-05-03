from django.shortcuts import render
from . import functions

# Create your views here.
from blog.models import News


def index (request):
    return render(request, 'blog/index.html')

def weather(request):
    realWeather = functions.getWeather()
    context = {
        'weather' : realWeather,
    }
    return render(request, 'blog/weather.html', context)

def news(request):
    #Получаем все новости
    allNews = News.objects.all().order_by("-time")

    #Передаём их в шаблон
    context = {
        'news': allNews,
    }
    return render(request, 'blog/news.html', context)

def about(request):
    return render(request, 'blog/about.html')