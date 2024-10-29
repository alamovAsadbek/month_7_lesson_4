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
def user_detail_view(request, pk):
    if request.method == 'GET':
        user = UserModel.objects.filter(pk=pk)
        serializer = UserModelSerializer(user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = request.data
        user = UserModel.objects.get(pk=pk)
        serializer = UserModelSerializer(user, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "User updated successfully", "data": serializer.data})
