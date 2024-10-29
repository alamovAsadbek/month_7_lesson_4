from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import *


@api_view(['GET', 'POST'])
def user_view(request):
    if request.method == 'GET':
        users = UserModel.objects.all()
        serializer = UserModelSerializer(users, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "User created successfully", "data": serializer.data})


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def user_detail_view(request, user_id):
    if request.method == 'GET':
        user = UserModel.objects.filter(pk=user_id)
        serializer = UserModelSerializer(user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = request.data
        user = UserModel.objects.get(pk=user_id)
        serializer = UserModelSerializer(user, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "User updated successfully", "data": serializer.data})
    elif request.method == 'DELETE':
        user = UserModel.objects.get(pk=user_id)
        user.delete()
        return Response({"message": "User deleted successfully"})
    elif request.method == 'PATCH':
        data = request.data
        user = UserModel.objects.get(pk=user_id)
        serializer = UserModelSerializer(user, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "User updated partially successfully", "data": serializer.data})
