from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer, CommentSerializer
from .models import Product, Comment
from django.shortcuts import get_object_or_404

# class DefaultsMixin(object):
#     authentication_classes = (
#         authentication.SessionAuthentication,
#         authentication.TokenAuthentication
#     )
#     permission_classes = (
#         IsAuthenticated
#     )
#     paginate_by = 25
#     paginate_by_param = 'page_size'
#     max_paginate_by = 100
#     filter_backends = (

#     )

# class ProductViewSet(ModelViewSet):
#     queryset = Product.available.all()
#     serializer_class =  ProductSerializer


class ProductListView(ListAPIView):
    pagination_class = LimitOffsetPagination
    paginate_by = 25
    queryset = Product.available.all()
    serializer_class = ProductSerializer



class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CommentCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, pk=product_id)
        serializer.save(author=self.request.user, product=product)



class ProductCommentsView(ListAPIView, LimitOffsetPagination):
    serializer_class = CommentSerializer
    default_limit = 10

    
    def get_queryset(self):
        product = get_object_or_404(Product, pk=self.kwargs.get('product_id'))
        return product.comments.all()

    

