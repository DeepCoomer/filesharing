from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FileListSerializer
from rest_framework.parsers import MultiPartParser
# from django.http import HttpResponse
from rest_framework import status

# Create your views here.

def home(request):
    return render(request ,'home.html')

def download(request , uid):
    return render(request , 'download.html' , context = {'uid' : uid})

class HandleFileUpload(APIView):

    parser_classes = [MultiPartParser]

    def post(self, request):
        try:
            data = request.data

            serializer = FileListSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'message': 'files uploaded successfully',
                    'data': serializer.data
                }, status=status.HTTP_200_OK)

            return Response({
                'message': 'somethign went wrong',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
