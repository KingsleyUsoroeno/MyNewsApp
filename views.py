from django.shortcuts import render
import requests
from django.http import HttpResponse


# Create your views here.

def fetchJsonData(request):
    url = 'https://newsapi.org/v2/everything?q=bitcoin&from=2019-01-01&sortBy=publishedAt&apiKey=b37668ef0d1e4ac283ad4c621cc396cf'
    newsData = requests.get(url=url).json()
    articlesArray = newsData['articles']
    return render(request, 'NewsApp/index.html', context={'articlesArray': articlesArray})
