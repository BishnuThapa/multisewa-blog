from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import Blog, CompanyInfo


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail', 'created_at')
    prepopulated_fields = {"slug": ("title",)}
    list_per_page = 10
    search_fields = ('title', 'description')

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50%;" />'.format(object.featured_image.url))


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'address')
