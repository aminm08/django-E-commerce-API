from django.contrib import admin
from .models import BlogPost


class BlogAdmin(admin.ModelAdmin):
    list_display = ('cover_preview', 'title', 'status', 'author', 'datetime_created', )


admin.site.register(BlogPost, BlogAdmin)