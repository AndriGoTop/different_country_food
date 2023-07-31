from django.shortcuts import render
from .models import Article, Country


def index(request):
    articles = Article.objects.all()
    countries = Country.objects.all()
    context = {
        'articles': articles,
        'countries': countries,
    }
    return render(request, 'articles/index.html', context)


def get_category(request, country_id):
    articles = Article.objects.filter(country_id=country_id)
    countries = Country.objects.all()
    country = Country.objects.get(pk=country_id)
    context = {
        'articles': articles,
        'countries': countries,
        'country': country,
    }
    return render(request, 'articles/country.html', context)


def article(request, article_id):
    articles = Article.objects.get(pk=article_id)
    pictures = articles.pictures.all()
    context = {
        'articles': articles,
        'pictures': pictures,
    }
    return render(request, 'articles/article.html', context)

