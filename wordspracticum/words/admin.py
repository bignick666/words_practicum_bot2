from django.contrib import admin
from .models import Word


class WordAdmin(admin.ModelAdmin):
    list_display = ['name', 'translate', 'category']
    list_display_links = ['name', 'translate', 'category']
    search_fields = ['name', 'translate']
    list_filter = ['category']


admin.site.register(Word, WordAdmin)

