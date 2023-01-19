from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from .permissions import UserPermission
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import ProductPagination, CommentPagination
from .serializers import ProductSerializer, CommentSerializer
from .models import Product

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = (UserPermission, )
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = ProductPagination
    search_fields = ['title', 'price']
    ordering_fields = ['discount', 'price', 'datetime_created']

    def get_queryset(self):
        if self.request.user.is_staff  :
            return Product.objects.all()
        return Product.available.all()



class CommentCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, pk=product_id)
        serializer.save(author=self.request.user, product=product)



class ProductCommentsView(ListAPIView):
    serializer_class = CommentSerializer
    pagination_class = CommentPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_filter = ['datetime_created', 'rating']

    
    def get_queryset(self):
        product = get_object_or_404(Product, pk=self.kwargs.get('product_id'))
        return product.comments.filter(active=True)

    

