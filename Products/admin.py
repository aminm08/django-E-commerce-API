from django.contrib import admin
from .models import Product,  Comment


class ProductAdmin(admin.ModelAdmin):
    ordering = ('-datetime_modified', )
    list_display = ('cover_preview', 'title', 'price', 'discount', 'active', 'datetime_created', 'datetime_modified', )
    search_fields = ('title', 'price')
    list_filter = ('active', )
    prepopulated_fields = {'slug':('title', )}

class CommentAdmin(admin.ModelAdmin):
    ordering = ('-datetime_created', )
    list_display = ('id', 'author', 'product', 'rating', 'active', 'datetime_created', )
    search_fields = ('author', 'product', )
    list_filter = ('rating', 'active', )

admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)