from rest_framework import pagination

class ProductPagination(pagination.LimitOffsetPagination):
    default_limit = 25
    max_limit = 75
    

class CommentPagination(pagination.LimitOffsetPagination):
    default_limit = 10
    max_limit = 20