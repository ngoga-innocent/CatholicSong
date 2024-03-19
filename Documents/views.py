from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Copies,SongType
from.serializers import CopiesSerializer,SongTypeSerializer
from rest_framework import status
# Create your views here.
class CopiesClass(APIView):
    def get(self,request):
        copy_id = request.query_params.get("copy_id") 
        if copy_id is not None:
            copy=get_object_or_404(Copies,id=copy_id)
            serializer=CopiesSerializer(instance=copy)
            return Response({"copy":serializer.data})
        else:
            copies=Copies.objects.all()
            serializer=CopiesSerializer(copies,many=True)
            return Response({"copies":serializer.data})
    def post(self,request):
        serializer=CopiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data})
        return Response({"detail":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request):
        copy_id=request.query_params.get('copy_id')
        if copy_id is not None:
            try:
                copy=get_object_or_404(Copies,id=copy_id)
                copy.delete()
                return Response({'details':'Copy deleted'})

            except Copies.DoesNotExist:
                return Response({'details':'Copies Does not Exist'},status=status.HTTP_404_NOT_FOUND) 
        else:
            return Response({'detail':'No copy has been provided'},status=status.HTTP_404_NOT_FOUND)
        
    def patch(self, request):
        copy_id=request.query_params.get('copy_id')
        if copy_id is not None:
            copy = get_object_or_404(Copies, id=copy_id)
            serializer = CopiesSerializer(instance=copy, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'copy':serializer.data})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"details":"copy id not provided"},status=status.HTTP_404_NOT_FOUND)
class SongTypeClass(APIView):
    def get(self,request):
        type_id = request.query_params.get("type_id") 
        if type_id is not None:
            try:
                type=SongType.objects.get(id=type_id)
                songs=Copies.objects.filter(category=type)
                serializer=CopiesSerializer(songs,many=True)
                return Response({'copies':serializer.data})
            except SongType.DoesNotExist():
                return Response({'detail':'The Type is not found'})
        else:
            types=SongType.objects.all()
            serializer=SongTypeSerializer(types,many=True)
            return Response({'types':serializer.data})

       
    
    

        
        