from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from feed import serializers
from feed import pagination
from feed import services


class PostListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.PostSerializer
    queryset = services.get_posts()
    pagination_class = pagination.PostsPagination

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_fields = ['user']

    permission_classes = [IsAuthenticatedOrReadOnly]


class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, pk):
        likes_count = services.like_post(request, pk)
        return Response({'total_likes_count': likes_count})


