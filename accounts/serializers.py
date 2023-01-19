from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'profile_image', 'first_name', 'last_name', )