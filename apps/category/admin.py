from django.contrib import admin


admin.site.site_header = "kun.uz Admin Paneli"
admin.site.site_title = "kun.uz Admin Paneli"
admin.site.index_title = "kun.uz Admin Paneliga Xush Kelibsiz!"


from .models import Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name', 'created_at', 'updated_at',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at',)
    search_fields = ('name',)
