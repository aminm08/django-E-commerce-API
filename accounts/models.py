from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', verbose_name=_('user profile image'), blank=True, null=True)
    
