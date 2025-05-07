from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'author',
        'painter',
        'image',
        'video',
        'views',
        'is_published',
        'created_at',
        'updated_at',
    )
    search_fields = ('name',)
