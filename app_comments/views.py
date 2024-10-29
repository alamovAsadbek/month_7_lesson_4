from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import *


@api_view(['GET', 'POST'])
def comments_view(request):
    if request.method == 'GET':
        comment = CommentModel.objects.all()
        serializer = CommentModelSerializer(comment, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CommentModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def comment_details_view(request, comment_id):
    if request.method == 'GET':
        comment = CommentModel.objects.filter(pk=comment_id)
        serializer = CommentModelSerializer(data=comment)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'PUT':
        data = request.data
        comment = CommentModel.objects.filter(pk=comment_id)
        serializer = CommentModelSerializer(data=data, instance=comment, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Comment updated successfully.", "data": serializer.data})
    elif request.method == 'DELETE':
        pass
    elif request.method == 'PATCH':
        pass


@api_view(['GET'])
def get_comment_by_blog_id_view(request, blog_id, user_id):
    if request.method == 'GET':
        pass
