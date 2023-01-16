from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from .serializers import ProductSerializer, CommentSerializer
from .models import Product, Comment
from django.shortcuts import get_object_or_404


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    # pagination_class = LimitOffsetPagination
    queryset = Product.objects.filter(active=True)


class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CommentCreateView(CreateAPIView):
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, pk=product_id)
        serializer.save(author=self.request.user, product=product)



class ProductCommentsView(ListAPIView):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        product = get_object_or_404(Product, pk=self.kwargs.get('product_id'))
        return product.comments.all()

    

