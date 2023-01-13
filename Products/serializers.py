from rest_framework import serializers
from .models import Product, Comment

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'discount', 'active', 'cover', 'slug')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    product = serializers.ReadOnlyField(source='product.title')
    class Meta:
        model = Comment
        fields = ('body', 'rating', 'author', 'product')
        
