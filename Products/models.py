from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
from django.urls import reverse

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self,**kwargs):
        defaults = {'min_value':self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class AvailableManager(models.Manager):
    def get_quesryset(self):
        return super(AvailableManager, self).get_queryset().filter(active=True, quantity__gte=1) 


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('product title'))
    description = RichTextField(verbose_name=_('product description'))
    price = models.PositiveIntegerField(default=0, verbose_name=_('product price'))
    discount = IntegerRangeField(min_value=0, max_value=100, verbose_name=_('discount on this product'), default=0)
    active = models.BooleanField(default=True, verbose_name=_('is this product available'))
    cover = models.ImageField(upload_to='product_covers/', verbose_name=_('Product cover'), blank=True)
    slug = models.SlugField(null=True)
    objects = models.Manager()
    available = AvailableManager()
    # category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE, related_name='products')

    datetime_created = models.DateTimeField(verbose_name=_('Creation date time'), default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)


    def __str__(self) :
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


    def get_final_price(self):
        return float(self.price - (self.price*self.discount/100))


    def cover_preview(self):
        return mark_safe(f"<img src='{self.cover.url}' width=70 height=70></img>")

    

class Comment(models.Model):
    RATING_CHOICES = (
        ('1', _('Very bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect')),
    )
    
    body = models.TextField(verbose_name=_('Comment text'))
    rating = models.CharField(choices=RATING_CHOICES, default='3', max_length=1, verbose_name=_('your score'))
    active = models.BooleanField(default=True, verbose_name=_('is this comment active'))

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}:{self.get_rating_display()}'