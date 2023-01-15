from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from .models import Order, OrderItem
from .serializers import OrderSerializer
from Cart.cart import Cart


class CreateOrderView(APIView):

    serializer_class = OrderSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        cart = Cart(request)
        if serializer.is_valid():
            serializer.save(user=request.user)
            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order=serializer.instance,
                    product = product,
                    quantity = item['quantity'],
                    price = product.get_final_price(),
                    )
            cart.clear()
            return Response({'order':str(serializer.instance)})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        

    