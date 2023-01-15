from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Order
        fields = ('user', 'first_name', 'last_name', 'phone_number', 'address', 'order_note', )
        