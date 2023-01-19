from django.db import models
from django.contrib.auth import get_user_model
class Favorite(models.Model):
    product = models.ForeignKey('Products.Product', on_delete=models.CASCADE, related_name='favorites')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='favorites')

    def __str__(self):
        return f'{self.user}:{self.product}'
