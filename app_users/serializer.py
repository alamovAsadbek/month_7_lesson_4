from rest_framework import serializers

from .models import *


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
        read_only_fields = ('id',)
