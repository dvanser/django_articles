from django.contrib import admin
from blog.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titleEn', 'slug', 'status', 'created')
    list_filter = ['tags']
    search_fields = ['titleEn', 'content']
    prepopulated_fields = {'slug': ['titleEn']}


admin.site.register(Article, ArticleAdmin)
