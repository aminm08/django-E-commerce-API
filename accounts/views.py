from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import UserProfileSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class UserProfileView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserProfileSerializer

    def get(self, request):
        user = get_object_or_404(get_user_model(), pk=request.user.id)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
   

    def put(self, request):
        user = get_object_or_404(get_user_model(), pk=request.user.id)
        serializer = UserProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    


