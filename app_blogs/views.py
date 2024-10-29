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
