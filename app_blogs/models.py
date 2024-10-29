from django.db import models
from rest_framework import serializers

from app_users.models import UserModel
from common.models import BaseModel


class BlogModel(BaseModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all())

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blogs'
        verbose_name_plural = 'Blogs'
        verbose_name = 'Blog'
