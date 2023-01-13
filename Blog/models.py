from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe
class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('p', 'Published'),
        ('d', 'Draft'),
    )

    title = models.CharField(max_length=100, verbose_name=_('blog title'))
    plain_description = models.TextField(_('short description'))
    text = RichTextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='blogs', verbose_name=_('blog author'))
    cover = models.ImageField(upload_to='blog_covers/', verbose_name=_('blog cover'))
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, verbose_name=_("blog's status"))

    def __str__(self):
        return self.title

    def cover_preview(self):
        return mark_safe(f"<img src='{self.cover.url}' width=70 height=70></img>")
