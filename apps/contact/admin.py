from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'phone_number',
        'subject',
        'file',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'name',
        'email',
        'phone_number',
        'subject',
    )
