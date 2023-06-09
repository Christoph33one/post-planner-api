from rest_framework import generics, permissions, filters
from planner_api.permissions import IsOwnerOrReadOnly
from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TravelPlan
from .serializers import TravelPlanSerializer
from planner_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class TravelPlanPostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = TravelPlanSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = TravelPlan.objects.annotate(
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        # To retreieve users post by the users ID
        'owner__followed__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        # To retreieve a travelplan by location
        'location',

    ]
    ordering_fields = [
        # To count comments added to a users post
        'comments_count',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TravelPlanPostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = TravelPlanSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = TravelPlan.objects.annotate(
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
