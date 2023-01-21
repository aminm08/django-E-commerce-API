from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('', views.WishListView.as_view(), name='wish_list'),
    path('delete/<int:product_id>/', views.WishDestroyView.as_view(), name='wish_delete')
]