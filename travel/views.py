from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TravelPlan
from .serializers import TravelPlanSerializer


# TravelPlanList view
class TravelPlanList(APIView):
    def get(self, request):
        travelplan = TravelPlan.objects.all()
        serializer = TravelPlanSerializer(
            travelplan, many=True, context={'request': request})
        return Response(serializer.data)
