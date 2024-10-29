from django.urls import path

from app_blogs.views import *
from app_users.views import *

urlpatterns = [
    path('blogs/', blogs_view, name='blogs'),
    path('users/', user_view, name='users'),
]
