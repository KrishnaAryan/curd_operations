from django.core.checks.messages import Error
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.
class RegisterViews(APIView):
    def get(self,request):
        obj=Register.objects.all()
        serializer=RegisterSerializer(obj, many=True)
        return Response({'status':200,'payload':serializer.data})

    def post(self,request):
        data=request.data
        serializer=RegisterSerializer(data=request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'errors':serializer.errors,'message':'something wrong'})

        serializer.save()
        print(data)
        return Response({'message':'send','payload':serializer.data})


    def patch(self,request):
        try:
            obj=Register.objects.get(id=request.data['id'])
            serializer=RegisterSerializer(obj,data=request.data, partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'errors':serializer.errors,'message':'something wrong'})

            serializer.save()
            return Response({'message':'data updated','payload':serializer.data})

        except Exception as e:
            print(e)
            return Response({'status':403,'message':'invalid id'})
            
    def delete(self,request):
        try:
        #we want to ?id=12 like this then
        #remove (request, id) form id only
        #id=request.GET.get('id') write here only
            id=request.GET.get('id')
            obj=Register.objects.get(id=id)
            obj.delete()
            return Response({'message':'deleted'})
        except Exception as e:
            print(e)
            return Response({'message':'invailed'})

