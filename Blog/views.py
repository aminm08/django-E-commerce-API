from rest_framework.viewsets import ModelViewSet
from .serializers import BlogSerializers
from .models import BlogPost
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from Products.permissions import UserPermission

class BlogPaginator(PageNumberPagination):
    page_size = 9
    

class BlogViewSet(ModelViewSet):
    serializer_class = BlogSerializers
    permission_classes = (UserPermission, )
    pagination_class = BlogPaginator
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'plain_description', 'author__username']
    ordering_fields = ['datetime_created']

    def get_queryset(self):
        if self.request.user.is_staff:
            return BlogPost.objects.all()
        return BlogPost.objects.filter(status='p')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)