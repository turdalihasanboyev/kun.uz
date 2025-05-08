from django.urls import path

from .views import HomePageView, ArticleDetailView, AboutPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('article-detail/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('about/', AboutPageView.as_view(), name='about'),
]
