from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework.filters import SearchFilter
from .models import Order, OrderItem
from .serializers import OrderSerializer
from Cart.cart import Cart




class CreateOrderView(APIView):
    permission_classes = (IsAuthenticated, )
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

        

class GetUserOrders(APIView):
    permission_classes = (IsAuthenticated, )
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_field = ['datetime_created', 'status', 'is_paid']
    search_field = ['first_name', 'last_name']

    def get(self, request):
        orders = request.user.orders.values()
        return Response(orders)