from django.db import models
from django.contrib.auth import get_user_model

class Wish(models.Model):
    product = models.ForeignKey('Products.Product', on_delete=models.CASCADE, related_name='wishes')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='wishes')


    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.user}:{self.product.id}'
