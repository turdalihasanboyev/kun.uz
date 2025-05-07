from django.contrib import admin

# from django.contrib.auth.admin import UserAdmin

from .models import Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Category admin interface.
    """

    model = Category

    ordering = ('-title',)

    search_fields = ('title',)

    prepopulated_fields = {'slug': ('title',)}

    list_filter = ('is_active',)

    list_display = (
        'id',
        'title',
        "is_active",
        "created_at",
        "updated_at",
    )

    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )

    fieldsets = (
        ('Personal info', {
            'fields': ('title', 'slug', 'parent', 'description',),
            'classes': ('wide',),
        }),
        ("Meta Dates", {
            'fields': ('created_at', 'updated_at',),
            'classes': ('wide', 'collapse',),
        }),
        ("ID", {
            'fields': ('id',),
            'classes': ('wide', 'collapse',), # yig'iladigan qilish
        }),
    )

    # add_fieldsets


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = (
        'id',
        'name',
        "is_active",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('is_active',)
    fieldsets = (
        ('Personal info', {
            'fields': ('name', 'slug',),
            'classes': ('wide',),
        }),
        ("Meta Dates", {
            'fields': ('created_at', 'updated_at',),
            'classes': ('wide', 'collapse',),
        }),
        ("ID", {
            'fields': ('id',),
            'classes': ('wide', 'collapse',), # yig'iladigan qilish
        }),
    )
