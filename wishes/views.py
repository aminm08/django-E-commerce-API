from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter
from rest_framework import status
from rest_framework.views import APIView
from Products.models import Product
from .serializers import WishSerializer
from .models import Wish

class WishListView(APIView):
    serializer_class = WishSerializer
    permission_classes = (IsAuthenticated, )
    
    

    def get(self, request):
        wishes = request.user.wishes.all().order_by('-datetime_created')
        serializer = self.serializer_class(wishes, many=True)
        return Response(serializer.data)


    def post(self, request):
        product = get_object_or_404(Product, pk=request.POST.get('product_id'))
        
        if not product.wishes.filter(user=request.user).exists():
            
            wish = Wish.objects.create(product=product, user=request.user)
            
            return Response({"wish":str(wish)}, status=status.HTTP_201_CREATED)
           
        return Response({'error':'this product is already in your wishlist'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class WishDestroyView(APIView):
    
    permission_classes = (IsAuthenticated, )

    
    def delete(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        wish = Wish.objects.filter(product=product, user=request.user)

        if wish.exists():
            print(wish)
            wish[0].delete()
            return Response({'message':'product deleted from wishlist'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'no such object'}, status=status.HTTP_404_NOT_FOUND)

        

