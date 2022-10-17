from rest_framework import serializers
from feed import models


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostLike
        fields = (
            'user',
            'post',
            'date',
        )


class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            'last_activity',
            'last_login',
            'date_joined',
        )