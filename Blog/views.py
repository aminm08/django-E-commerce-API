from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import BlogSerializers
from .models import BlogPost

class BlogListView(ListAPIView):
    
    serializer_class = BlogSerializers
    queryset = BlogPost.objects.filter(status='p')

class BlogDetailView(RetrieveAPIView):
    serializer_class = BlogSerializers
    queryset = BlogPost.objects.filter(status='p')
