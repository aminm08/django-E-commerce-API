from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', views.ProductViewSet, basename='product')


urlpatterns = [
  
    path('<int:product_id>/comments', views.ProductCommentsView.as_view(), name='product_comments'),
    path('<int:product_id>/comments/add/', views.CommentCreateView.as_view(), name='comment_create'),
]
urlpatterns += router.urls