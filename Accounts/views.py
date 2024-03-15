from django.shortcuts import render,get_object_or_404
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Users
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class RegisterView(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user=get_object_or_404(Users,username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            return Response(serializer.data)
        return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
class LoginView(APIView):
    def post(self,request):
        user =get_object_or_404(Users,username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response({"detail":'Passwords doesnot match'},status=status.HTTP_400_BAD_REQUEST)
        token,created=Token.objects.get_or_create(user=user)
        serializer=UserSerializer(instance=user)
        return Response({"token":token.key,"user":serializer.data})
@api_view(['GET'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def TokenVerification(request):
    return Response({"user":format(UserSerializer(instance=request.user).data)}) 

@api_view(['PUT'])
def ResetPassword(request):
    try:
        user=Users.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        serializer=UserSerializer(instance=user)
        return Response({'user':serializer.data})
    except Users.DoesNotExist:
        return Response({'detail':'user Not found'},status=status.HTTP_404_NOT_FOUND)
    