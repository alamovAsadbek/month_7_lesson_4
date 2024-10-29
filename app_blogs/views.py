from rest_framework.decorators import api_view


@api_view(['GET'])
def blogs_view(request):
    if request.method == 'GET':
        pass
