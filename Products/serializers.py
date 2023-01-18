from rest_framework import serializers
from .models import Product, Comment

class ProductSerializer(serializers.ModelSerializer):
    product_absolute_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'discount', 'active', 'cover', 'slug', 'product_absolute_url')


    def get_product_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.get_absolute_url())


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    product = serializers.ReadOnlyField(source='product.title')
    class Meta:
        model = Comment
        fields = ('id', 'body', 'rating', 'author', 'product')

    
        
