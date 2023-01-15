from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.response import Response
from Products.models import Product
from .cart import Cart
from .serializers import CartSerializer


class GetCartItems(APIView):

    
    def get(self, request):
        cart = Cart(request)
        items = []
        for i in cart:
            obj = i['product_obj']
            product = {
                'title':obj.title,
                'price':obj.price,
                'discount':obj.discount,
                'cover':obj.cover.url,
                }
            i['product_obj'] = product
            items.append(i)
        
        return Response(items)


class AddCartItem(APIView):
    serializer_class = CartSerializer

    def post(self, request, product_id):
        
        product = get_object_or_404(Product, pk=product_id)
        serializer = self.serializer_class(data=request.data)
        cart = Cart(request)
        
        if serializer.is_valid():
            data = serializer.validated_data
            cart.add(product, data['quantity'], data['inplace'])
        
            return Response({'cart':str(cart)})
        else:

            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST 
                )
        

class RemoveFromCart(APIView):

    def delete(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        cart = Cart(request)
        print(cart)
        cart.remove(product)
        return Response(str(cart))


class ClearCart(APIView):
    def delete(self, request):
        cart = Cart(request)
        if len(cart):
            cart.clear()
            return Response({'message':'cart cleared'})
        return Response({'message':'cart is already empty'})
