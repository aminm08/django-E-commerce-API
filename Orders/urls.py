from django.urls import path

from . import views

urlpatterns= [
    path('create/', views.CreateOrderView.as_view(), name='create_order'),
    path('get_orders/', views.GetUserOrders.as_view(), name='get_orders'),
]