from rest_framework import serializers
from instagram.models.post import Post, Like


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'description', 'image', 'author', 'created', 'updated')
        read_only_fields = ('id', 'author', 'created', 'updated')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user', 'post')
        read_only_fields = ('id',)
