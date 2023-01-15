from rest_framework import serializers


class CartSerializer(serializers.Serializer):

    quantity = serializers.IntegerField(min_value=0, max_value=30)
    inplace = serializers.BooleanField(required=False)