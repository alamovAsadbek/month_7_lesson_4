from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import *


@api_view(['GET', 'POST'])
def blogs_view(request):
    if request.method == 'GET':
        blogs = BlogModel.objects.all()
        serializer = BlogModelSerializer(blogs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BlogModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"message": "Blog created successfully", "data": serializer.data})


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def blog_detail_view(request, blog_id):
    if request.method == 'GET':
        blog = get_object_or_404(BlogModel, pk=blog_id)
        serializer = BlogModelSerializer(blog)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        blog = get_object_or_404(BlogModel, pk=blog_id)
        serializer = BlogModelSerializer(blog, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Blog updated successfully", "data": serializer.data})
    elif request.method == 'DELETE':
        blog = get_object_or_404(BlogModel, pk=blog_id)
        blog.delete()
        return Response({"message": "Blog deleted successfully"})
    elif request.method == 'PATCH':
        blog = get_object_or_404(BlogModel, pk=blog_id)
        serializer = BlogModelSerializer(blog, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Blog updated partially successfully", "data": serializer.data})


@api_view(['GET'])
def get_blog_by_user_id(request, user_id, blog_id):
    if request.method == 'GET':
        blog = get_object_or_404(BlogModel, pk=blog_id, user=user_id)
        serializer = BlogModelSerializer(blog)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
