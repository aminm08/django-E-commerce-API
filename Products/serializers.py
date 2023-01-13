from rest_framework import serializers
from .models import Product, Comment

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'discount', 'active', 'cover', 'slug')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    product = serializers.ReadOnlyField(source='product.title')
    class Meta:
        model = Comment
        fields = ('id', 'body', 'rating', 'author', 'product')
        
