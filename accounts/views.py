from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from.serializers import UserSerializer, UpdatePasswordSerializer


class RegisterView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class MeView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
class UpdatePasswordView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, format=None):
        serializer = UpdatePasswordSerializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
