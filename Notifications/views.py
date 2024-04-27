from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import NotificationModal
from .serializers import NotificationSeriazer
# Create your views here.

class NotificationView(APIView):
    def get(self,request):
        notifications=NotificationModal.objects.all()
        seriazer=NotificationSeriazer(notifications,many=True)
        return Response({"notifications":seriazer.data},status=200)
    def put(self,request,pk):
        try:
            notification=NotificationModal.objects.get(pk=pk)

        except NotificationModal.DoesNotExist:
            return Response({"details":"provided notfication Does not exists"},status=404)
        serializer=NotificationSeriazer(notification,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"details":"notification updated successfull"},status=200)
        else:
            return Response({"errors":serializer.errors},status=401)
        
    def delete(self,request,pk):
        try:
            notification=NotificationModal.objects.get(pk=pk)
            notification.delete()
            return Response({"details":"Notification deleted Successfully"})
        except NotificationModal.DoesNotExist:
            return Response({"error":"provided notification does not exist"},status=404)
        

