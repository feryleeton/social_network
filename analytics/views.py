from django_filters import rest_framework as drf_filters

from rest_framework import generics

from analytics import filters
from analytics import serializers
from analytics import pagination
from analytics import services


class LikeActivityAnalytics(generics.ListAPIView):
    queryset = services.get_post_likes()
    serializer_class = serializers.PostLikeSerializer
    pagination_class = pagination.AnalyticsPagination

    filter_backends = (drf_filters.DjangoFilterBackend,)
    filterset_class = filters.DateRangeFilterSet


class UserActivityAnalytics(generics.RetrieveAPIView):
    queryset = services.get_users()
    serializer_class = serializers.UserActivitySerializer
