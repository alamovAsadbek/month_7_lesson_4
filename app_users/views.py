from rest_framework.response import Response

from .serializer import *


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
