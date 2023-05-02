from django.urls import path
from travel import views

urlpatterns = [
    path('travelplanposts/', views.TravelPlanPostList.as_view()),
    path('posts/<int:pk>/', views.TravelPlanPostDetail.as_view()),
    ]
