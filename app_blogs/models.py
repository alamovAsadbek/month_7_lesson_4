from django.db import models


class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
