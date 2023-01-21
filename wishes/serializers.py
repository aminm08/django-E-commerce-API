from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Wish


class WishSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.username')
    product = ReadOnlyField(source='product.title')
    class Meta:
        model = Wish
        fields = '__all__'