from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('<int:product_id>/comments', views.ProductCommentsView.as_view(), name='product_comments'),
    path('<int:product_id>/comments/add/', views.CommentCreateView.as_view(), name='comment_create'),
]