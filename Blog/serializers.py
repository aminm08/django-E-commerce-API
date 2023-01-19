from rest_framework import serializers
from .models import BlogPost

class BlogSerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post_absolute_url = serializers.SerializerMethodField()
    class Meta:
        model = BlogPost
        fields = ('title', 'plain_description', 'text', 'author', 'cover', 'status', 'post_absolute_url', )

    def get_post_absolute_url(self, obj):
        return self.context.get('request').build_absolute_uri(obj.get_absolute_url())