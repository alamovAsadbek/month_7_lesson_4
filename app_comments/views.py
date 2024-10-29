from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def comments_view(request):
    if request.method == 'GET':
        # Get all comments
        pass
    elif request.method == 'POST':
        # Create a new comment
        pass
