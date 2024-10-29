from django.urls import path

from app_blogs.views import *

urlpatterns = [
    path('blogs/', blogs_view, name='blogs')
]
