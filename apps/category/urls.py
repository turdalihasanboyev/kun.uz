from django.urls import path

from .views import CategoryView


urlpatterns = [
    path('category/articles/<slug:slug>/', CategoryView.as_view(), name='category'),
]
