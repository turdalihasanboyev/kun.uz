from django.shortcuts import render
from django.views import View

from apps.article.models import Article


class CategoryView(View):
    def get(self, request, slug):
        articles = Article.objects.filter(category__slug__exact=slug)
        return render(request, 'category.html', {'articles': articles})
