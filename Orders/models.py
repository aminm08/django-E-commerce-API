from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
class Order(models.Model):
    ORDER_STATUS_CHOICES =(
        ('su', _('submitted')),
        ('pr', _('proccesing')),
        ('de', _('deleiverd')),
        )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    is_paid = models.BooleanField(default=False)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=700)
    status = models.CharField(choices=ORDER_STATUS_CHOICES, max_length=2, null=True)
    order_note = models.CharField(max_length=700, blank=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'order {self.pk} for ({self.first_name} {self.last_name})'


class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('Products.Product', on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'order {self.order.pk}, product{self.product.pk} x {self.quantity}'

    def cover_preview(self):
        return mark_safe(f"<img src='{self.product.cover.url}' width=70 height=70></img>")
