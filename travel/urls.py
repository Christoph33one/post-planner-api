from django.urls import path
from travel import views

urlpatterns = [
    path('travelplan/', views.TravelPlanList.as_view()),
    ]
