# from django.contrib.auth.models import User
# from .models import TravelPlan
# from rest_framework import status
# from rest_framework.test import APITestCase


# class TravelPlanPostViewList(APITestCase):
#     def setUp(self):
#         User.objects.create_user(username='chris', password='pass')

#     # User to view a list of posts
#     def test_can_list_posts(self):
#         chris = User.objects.get(username='chris')
#         TravelPlan.objects.create(owner=chris, title='a title')
#         response = self.client.get('/travelplanposts/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         print(response.data)
#         print(len(response.data))

#     # User can create a post
#     def test_logged_in_user_can_create_post(self):
#         self.client.login(username='chris', password='pass')
#         response = self.client.post('/travelplanposts/', {'title': 'a title', 'description': 'test', 'location': 'test location'})
#         count = TravelPlan.objects.count()
#         self.assertEqual(count, 1)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     # Unauthorised user can not create a post
#     def test_user_not_logged_in_cant_create_post(self):
#         response = self.client.post('/travelplanposts/', {'title': 'a title', 'description': 'test', 'location': 'test location'})
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


# class TravelPlanPostDetailViewTest(APITestCase):
#     def setUp(self):
#         chris = User.objects.create_user(username='chris', password='pass')
#         brian = User.objects.create_user(username='brian', password='pass')
#         TravelPlan.objects.create(
#             owner=chris, title='a title', description='chris description'
#         )
#         TravelPlan.objects.create(
#             owner=chris, title='a title', description='chris description'
#         )

#     # retieve a post using a valid post ID
#     def test_can_retrieve_post_using_valid_id(self):
#         response = self.client.get('/posts/1/')
#         self.assertEqual(response.data['title'], 'a title')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     # Can not retieve a post using the wrong post ID
#     def test_cant_retrieve_post_using_invalid_id(self):
#         response = self.client.get('/posts/999/')
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

#     # User can update their post with the correct user ID
#     def test_user_can_update_own_post(self):
#         self.client.login(username='chris', password='pass')
#         response = self.client.put('/posts/1/', {'title': 'a new title', 'description': 'testing', 'location': 'testing location'})
#         post = TravelPlan.objects.filter(pk=1).first()
#         self.assertEqual(post.title, 'a new title')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     # An unauthorised user can not update another users post
#     def test_user_cant_update_another_users_post(self):
#         self.client.login(username='adam', password='pass')
#         response = self.client.put('/posts/2/', {'title': 'a new title', 'description': 'testing', 'location': 'testing location'})
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
