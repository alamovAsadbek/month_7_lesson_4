from django.urls import path

from app_blogs.views import *
from app_users.views import *
from app_comments.views import *
urlpatterns = [
    path('blogs/', blogs_view, name='blogs'),
    path('blogs/<int:blog_id>/', blog_detail_view, name='blog_detail'),
    path('blogs/<int:user_id>/<int:blog_id>/', blogs_view, name='blog_create'),
    path('users/', user_view, name='users'),
    path('users/<int:user_id>/', user_detail_view, name='user_detail'),
    path('comments/', comments_view, name='comments'),
    path('comments/<int:comment_id>/', comment_details_view, name='comment_detail'),
    path('comments/<int:blog_id>/<int:user_id>/', get_comment_by_blog_id_view, name='comment_create'),
]
