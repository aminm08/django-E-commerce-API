from django.urls import path

from . import views


urlpatterns = [
    path('', views.GetCartItems.as_view(), name='cart'),
    path('add/<int:product_id>/', views.AddCartItem.as_view(), name='add_cart'),
    path('remove/<int:product_id>/', views.RemoveFromCart.as_view(), name='remove_cart'),
    path('clear/', views.ClearCart.as_view(), name='clear_cart'),
    path('get_final_price/', views.get_final_price_view, name='final_price'),
]