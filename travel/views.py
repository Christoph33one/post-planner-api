from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TravelPlan
from .serializers import TravelPlanSerializer
from planner_api.permissions import IsOwnerOrReadOnly


# TravelPlanList view
class TravelPlanPostList(APIView):
    serializer_class = TravelPlanSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        travelplan = TravelPlan.objects.all()
        serializer = TravelPlanSerializer(
            travelplan, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = TravelPlanSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class TravelPlanPostDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TravelPlanSerializer

    def get_object(self, pk):
        try:
            post = TravelPlan.objects.get(pk=pk)
            self.check_object_permissions(self.request, post)
            return post
        except TravelPlan.DoesNotExist:
            raise Http404()

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = TravelPlanSerializer(
            post, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = TravelPlanSerializer(
            post, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
