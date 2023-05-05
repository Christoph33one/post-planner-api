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
        'owner__profile',
    ]
    search_fields = [
        # To retreieve a travelplan by location
        'location',

    ]
    ordering_fields = [
        'comments_count',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# # TravelPlanList view
# class TravelPlanPostList(APIView):
#     serializer_class = TravelPlanSerializer
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly
#     ]

#     def get(self, request):
#         travelplan = TravelPlan.objects.all()
#         serializer = TravelPlanSerializer(
#             travelplan, many=True, context={'request': request})
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = TravelPlanSerializer(
#             data=request.data, context={'request': request}
#         )
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(
#                 serializer.data, status=status.HTTP_201_CREATED
#             )
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST
#         )


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


# class TravelPlanPostDetail(APIView):
#     permission_classes = [IsOwnerOrReadOnly]
#     serializer_class = TravelPlanSerializer

#     def get_object(self, pk):
#         try:
#             post = TravelPlan.objects.get(pk=pk)
#             self.check_object_permissions(self.request, post)
#             return post
#         except TravelPlan.DoesNotExist:
#             raise Http404()

#     # Get users post by user id
#     def get(self, request, pk):
#         post = self.get_object(pk)
#         serializer = TravelPlanSerializer(
#             post, context={'request': request}
#         )
#         return Response(serializer.data)

#     # edit users post by user id
#     def put(self, request, pk):
#         post = self.get_object(pk)
#         serializer = TravelPlanSerializer(
#             post, data=request.data, context={'request': request}
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST
#         )

#     # Delete users post by user id
#     def delete(self, request, pk):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT
#         )
