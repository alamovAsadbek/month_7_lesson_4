from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def comments_view(request):
    if request.method == 'GET':
        # Get all comments
        pass
    elif request.method == 'POST':
        # Create a new comment
        pass


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def comment_details_view(request, comment_id):
    pass


@api_view(['GET'])
def get_comment_by_blog_id_view(request, blog_id, user_id):
    pass
