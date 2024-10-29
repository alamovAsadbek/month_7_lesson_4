from django.urls import path

from app_blogs.views import *
from app_users.views import *

urlpatterns = [
    path('blogs/', blogs_view, name='blogs'),
    path('blogs/<int:blog_id>/', blog_detail_view, name='blog_detail'),
    path('users/', user_view, name='users'),
    path('users/<int:user_id>/', user_detail_view, name='user_detail')
]
