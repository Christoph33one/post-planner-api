from django.db.models import Count
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from planner_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__travelplan', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        # DRF filtering by owner__profile field.
        'owner__profile',
    ]
    ordering_fields = [
        # To calculate the amount the post per user
        'posts_count',
    ]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a profile if you're the owner.
    """
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__travelplan', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
