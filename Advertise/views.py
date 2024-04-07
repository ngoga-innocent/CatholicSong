from django.shortcuts import render
from rest_framework.views import APIView
from .models import Event,EventImage,TrendingSongs
from .serializers import EventSerializer,EventImageSerializer,TrendingSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class Adverts(APIView):
    def get(self,request):
        event_id=request.GET.get('id',None)
        if event_id:
            try:
                event=Event.objects.get(pk=event_id)
                event_images=EventImage.objects.filter(event=event_id)
                event_serializer=EventSerializer(event,context={'request':request},many=True)
                event_image_serializer=EventImageSerializer(event_images,context={"request":request},many=True)

                return Response({'event':event_serializer,'event_image':event_image_serializer})
            except Event.DoesNotExist:
                return Response({"detail":'No event found'},status=status.HTTP_204_NO_CONTENT)
        else:
            event=Event.objects.all()
            serializer=EventImageSerializer(event,context={"request":request},many=True)
            return Response({'events':serializer.data},status=status.HTTP_200_OK)
class Trending(APIView):
    def get(self,request):
        trending=TrendingSongs.objects.all()
        serializer=TrendingSerializer(trending,context={'request':request},many=True)
        return Response({'trending':serializer.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=TrendingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response":serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response({"details":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
