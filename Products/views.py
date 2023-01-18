from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import ProductPagination, CommentPagination
from .serializers import ProductSerializer, CommentSerializer
from .models import Product, Comment




class ProductListView(ListAPIView):
    pagination_class = ProductPagination
    queryset = Product.available.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    search_fields = ['title', 'price']
    ordering_fields = ['discount', 'price']
    


class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.available.all()
    


class CommentCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, pk=product_id)
        serializer.save(author=self.request.user, product=product)



class ProductCommentsView(ListAPIView):
    serializer_class = CommentSerializer
    pagination_class = CommentPagination

    
    def get_queryset(self):
        product = get_object_or_404(Product, pk=self.kwargs.get('product_id'))
        return product.comments.all()

    

