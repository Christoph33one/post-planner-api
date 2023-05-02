from django.contrib.auth.models import User
from .models import TravelPlan
from rest_framework import status
from rest_framework.test import APITestCase


class TravelPlanPostViewList(APITestCase):
    def setUp(self):
        User.objects.create_user(username='chris', password='pass')

    def test_can_list_posts(self):
        chris = User.objects.get(username='chris')
        TravelPlan.objects.create(owner=chris, title='a title')
        response = self.client.get('/travelplanposts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='chris', password='pass')
        response = self.client.post('/travelplanposts/', {'title': 'a title', 'description': 'test', 'location': 'test location'})
        count = TravelPlan.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        response = self.client.post('/travelplanposts/', {'title': 'a title', 'description': 'test', 'location': 'test location'} )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
