from rest_framework.viewsets import ModelViewSet
from .serializer import PostSerializer, LikeSerializer
from django.shortcuts import get_object_or_404
from instagram.models.post import Post, Like
from rest_framework.response import Response
from .permission import IsCurrentUser
from rest_framework.permissions import IsAuthenticated


class PostAPIView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsCurrentUser, IsAuthenticated]


class LikeAPIView(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
