from re import search
from django.shortcuts import render
from rest_framework import serializers
import rest_framework
from rest_framework import permissions
from rest_framework import response
from rest_framework.views import APIView
from .models import Blog
from .serializer import BlogSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import request, HttpResponse
from rest_framework.views import APIView
from rest_framework import generics,mixins
from rest_framework.authentication import BasicAuthentication, SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
# Create your views here.

# This is function base views using @apiview decorator 

# @api_view(['GET','POST'])
# def BlogApi(request):
#     if request.method=='GET':
#         blog= Blog.objects.all()
#         serializer= BlogSerializer(many= True)
#         return Response(serializer.data)
#     elif request.method=='POST':
#         serializer= BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def BlogApiDetail(request,pk):
#     blog = Blog.objects.get(pk=pk)
#     if request.method == 'GET':
#         seralizer = BlogSerializer(blog)
#         return Response(seralizer.data)
#     elif request.method=='PUT':
#         seralizer = BlogSerializer(blog,data=request.data)
#         if seralizer.is_valid():
#             seralizer.save()
#             return Response(seralizer.data)
#         else:
#             return Response(seralizer.error)
        
#     elif request.method == 'DELETE':
#         blog.delete()
#         return HttpResponse('Deleted')


# this is classbase view

# class BlogApi(APIView):   
#     def get(self,request):
#         blog=Blog.objects.all()
#         serializer= BlogSerializer(blog,many= True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer= BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
            

# class BlogApiDetail(APIView):
#     def get(self,request,pk=None):
#          blog = Blog.objects.get(pk=pk)
#          serializer= BlogSerializer(blog)
#          return Response(serializer.data)


#     def put(self,request,pk=None):
#         blog=Blog.objects.get(pk=pk)
#         serailizer = BlogSerializer(blog,data=request.data)
#         if serailizer.is_valid():
#             serailizer.save()   
#             return Response(serailizer.data)
#         else:
#             return Response(serailizer.error)

#     def delete(self,request,pk=None):
#         blog=Blog.objects.get(pk=pk)
#         blog.delete()
#         return Response(status=200)


# Class base view with generic and mixins
# class BlogApi(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
#     serializer_class = BlogSerializer
#     queryset = Blog.objects.all()
#     authentication_classes =[TokenAuthentication]
#     permission_classes = [IsAuthenticated]
    
    
#     def get(self,request):
#         return self.list(request)

    
#     def post(self,request):
#         return self.create(request)

    
   



# class BlogDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
#     serializer_class = BlogSerializer
#     queryset = Blog.objects.all()
#     lookup_field= 'pk'
    

#     def get(self,request,pk=None):
#         return self.retrieve(request,pk)

    
#     def put(self,request, pk=None):
#         return self.update(request,pk)


#     def delete(self,request,pk=None):
#         return self.destroy(request,pk)



#Viewset

# class BlogView(viewsets.ViewSet):
    

#     def list(self,request):
#         blog= Blog.objects.all()
#         serializer= BlogSerializer(blog,many=True)
#         return Response(serializer.data)

#     def create(self,request):
#         serializer=BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.error)

#     def retrieve(self,request,pk=None):
#         queryset = Blog.objects.all()
#         blog = get_object_or_404(queryset, pk=pk)
#         serializer= BlogSerializer(blog)
#         return Response(serializer.data)


#     def update(self,request,pk=None):
#         blog= Blog.objects.get(pk=pk)
#         serializer=BlogSerializer(blog,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.error)


#     def destroy(self,request,pk=None):
#         blog= Blog.objects.get(pk=pk)
#         blog.delete()
#         return Response(status=200)



class BlogView(viewsets.ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer



















