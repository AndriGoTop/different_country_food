from django.contrib import admin

from .models import Article, Country, Pictures


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at', 'country']
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)
    list_filter = ('country',)


class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)


class PicturesAdmin(admin.ModelAdmin):
    list_display = ['id', 'picture']
    list_display_links = ('id',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Pictures, PicturesAdmin)
