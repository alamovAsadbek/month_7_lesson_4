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
def blog_detail_view(request, pk):
    if request.method == 'GET':
        blog = get_object_or_404(BlogModel, pk=pk)
        serializer = BlogModelSerializer(blog)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
