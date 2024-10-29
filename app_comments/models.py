from django.db import models
from rest_framework import serializers

from app_blogs.models import BlogModel
from app_users.models import UserModel
from common.models import BaseModel


class CommentModel(BaseModel):
    content = models.TextField()
    user = serializers.PrimaryKeyRelatedField(queryset='UserModel.objects.all()', required=True)
    post = serializers.PrimaryKeyRelatedField(queryset='BlogModel.objects.all()', required=True)

    class Meta:
        db_table = 'app_comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.content
