from django.shortcuts import render
from rest_framework import serializers
from .models import Blog
from .serializer import BlogSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import request

# Create your views here.

@api_view(['GET','POST'])
def BlogApi(request):
    if request.method=='GET':
        blog= Blog.objects.all()
        serializer= BlogSerializer(blog,many= True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer= BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)




