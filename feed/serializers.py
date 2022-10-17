from rest_framework import serializers
from feed import models


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostImage
        fields = ('image',)


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    images = PostImageSerializer(source='postimage_set', many=True, read_only=True)
    likes_count = serializers.SerializerMethodField(method_name='get_likes_count')

    class Meta:
        model = models.Post
        fields = (
            'id',
            'title',
            'text',
            'images',
            'likes_count',
            'date_created',
            'user',
        )

    def get_likes_count(self, obj):
        return models.PostLike.objects.filter(post=obj).count()

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES.getlist('images')
        post = models.Post.objects.create(
            title=validated_data.get('title', 'no-title'),
            text=validated_data.get('text'),
            user_id=self.context['request'].user.pk
        )
        for image_data in images_data:
            models.PostImage.objects.create(post=post, image=image_data)
        return post