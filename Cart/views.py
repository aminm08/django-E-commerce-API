from django.shortcuts import render
from .cart import Cart
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Products.models import Product
@api_view()
def get_cart(request):
    p = Product.objects.last()
    cart=Cart(request)
    cart.add(p, 2, replace_current_quantity=True)
    return Response({'h':'hello'})