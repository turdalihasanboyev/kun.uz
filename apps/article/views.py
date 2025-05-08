from django.shortcuts import render

from django.views import View

from apps.category.models import Category, Tag
from apps.article.models import Article


class HomePageView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')

        articles = Article.objects.all()

        if q:
            articles = articles.filter(name__icontains=q)

        context = {'articles': articles[:6]}

        return render(request, self.template_name, context)


class ArticleDetailView(View):
    template_name = 'article_detail.html'

    def get(self, request, slug, *args, **kwargs):
        article = Article.objects.get(slug__exact=slug)
        article.views += 1
        article.save()

        article_category = Article.objects.filter(category__slug__iexact=article.category.slug).exclude(slug__iexact=article.slug).order_by('id')[:4]

        context = {
            'article': article,
            'article_category': article_category,
        }

        return render(request, self.template_name, context)


class AboutPageView(View):
    def get(self, request):
        return render(request, 'about.html')
