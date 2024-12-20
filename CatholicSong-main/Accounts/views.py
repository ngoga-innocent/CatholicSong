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
from rest_framework.authentication import get_authorization_header
from django.db.models import Q
# Create your views here.
class RegisterView(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user=get_object_or_404(Users,username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            print(serializer.data)
            return Response(serializer.data)
        print(serializer.errors)
        return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
class LoginView(APIView):
    def post(self,request):
        username = request.data.get('username')
        
        password = request.data.get('password')
        user =get_object_or_404(Users,Q(username=username) | Q(phone_number=username))
        if not user.check_password(request.data['password']):
            return Response({"detail":'Passwords doesnot match'},status=status.HTTP_400_BAD_REQUEST)
        token,created=Token.objects.get_or_create(user=user)
        serializer=UserSerializer(instance=user)
        return Response({"token":token.key,"user":serializer.data})

def TokenVerification(auth_token):
    # auth_token=request.META.get('HTTP_AUTHORIZATION')
    print(auth_token)
    if not auth_token:
        return Response({'detail':'No token '},status=403)
    else:
        try:
            
            token_prefix=auth_token.split(' ')[0]
            
            if token_prefix.lower() != 'token':
                return Response({'detail':'invalid token prefix'},status=403)
            user_token=Token.objects.get(key=auth_token.split(' ')[1])
            # user=UserSerializer(user_token.user,context={"request":request})
            # return Response({"user":user.data},status=200)
            print(user_token)
            return user_token.user
        except:
            return Response({'detail':'invalid Token'},status=401)

# @authentication_classes([SessionAuthentication,TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def TokenVerification(request):
#     return Response({"user":format(UserSerializer(instance=request.user).data)}) 

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
@api_view(['PUT'])
def UpdateProfile(request):
        auth_token=request.META.get('HTTP_AUTHORIZATION')
        user = TokenVerification(auth_token)
        if not user:
            return Response({'detail':'Please Login'})
        try:
            user_object=Users.objects.get(pk=user.id)
            serializer=UserSerializer(user_object,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"detail":serializer.data})
            else:
                print(serializer.errors)
                return Response({"detail":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Users.DoesNotExist:
            return Response({'detail':'user not found'},status=status.HTTP_401_UNAUTHORIZED)
@api_view(['GET'])
def GetProfile(request):
    auth_token=request.META.get('HTTP_AUTHORIZATION')
    user = TokenVerification(auth_token)
    print(user)
    if not user:
        return Response({"detail":'please Login'})
 
    # return Response("ok")
    
    try:
        user_object=Users.objects.get(pk=user.id)
        serializer=UserSerializer(user_object,context={"request":request})
        
        return Response({'user':serializer.data})
    except Users.DoesNotExist:
        return Response({"detail":"No user found"})
