from rest_framework import serializers
from .models import BlogPost

class BlogSerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = BlogPost
        fields = ('title', 'plain_description', 'text', 'author', 'cover', 'status', )