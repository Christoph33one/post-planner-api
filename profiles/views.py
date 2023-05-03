from rest_framework import generics
from planner_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# # Profile list view.
# class ProfileList(APIView):
#     def get(self, request):
#         profiles = Profile.objects.all()
#         serializer = ProfileSerializer(
#             profiles, many=True, context={'request': request})
#         return Response(serializer.data)


class ProfileDetail(generics.RetrieveAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Profile detial view
# class ProfileDetail(APIView):
#     serializer_class = ProfileSerializer
#     permission_classes = [IsOwnerOrReadOnly]

#     def get_object(self, pk):
#         try:
#             profile = Profile.objects.get(pk=pk)
#             self.check_object_permissions(self.request, profile)
#             return profile
#         except Profile.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         profile = self.get_object(pk)
#         serializer = ProfileSerializer(
#             profile, context={'request': request})
#         return Response(serializer.data)

#     # PUT method
#     def put(self, request, pk):
#         profile = self.get_object(pk)
#         serializer = ProfileSerializer(
#             profile, data=request.data, context={'request': request}
#             )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
