from django.contrib.auth.models import User
from .models import Profile
from rest_framework import status
from rest_framework.test import APITestCase


class ProfileListViewTests(APITestCase):
    def setUp(self):
        chris = User.objects.create_user(username='chris', password='testpass')
        brian = User.objects.create_user(username='brian', password='testpass')

    def test_profile_automatically_created_on_user_creation(self):
        """
        Test create users profile after user is authenticated
        """
        response = self.client.get('/profiles/')
        count = Profile.objects.count()
        self.assertEqual(count, 2)

    def test_can_list_profiles(self):
        """
        Test a list pf profile can be viewed
        """
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProfileDetailViewTests(APITestCase):
    def setUp(self):
        chris = User.objects.create_user(username='chris', password='testpass')
        brian = User.objects.create_user(username='brian', password='testpass')

    def test_cant_retrieve_profile_using_invalid_id(self):
        """
        Test invaild user Id against retrieving correct user Id profile
        """
        response = self.client.get('/profiles/999/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_retrieve_profile_using_valid_id(self):
        """
        Test vaild user Id can retrieve the mathcing profile
        """
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # pass 403 ????

    def test_logged_in_user_can_update_their_profile(self):
        """
        Test authenticated user can update their profile
        """
        self.client.login(username='chris', password='testpass')
        response = self.client.put(
            '/profiles/1/', {'name': 'christopher'}
        )
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.name, 'christopher')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_other_profiles(self):
        """
        Test unauthorised user can not update a profile
        """
        self.client.login(username='vicky', password='testpass')
        response = self.client.put(
            '/profiles/1/', {'bio': 'try to edit a profile'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_their_profile(self):
        """
        Test authenticated user can delete their profile
        """
        self.client.login(username='chris', password='testpass')
        response = self.client.delete('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_user_cant_delete_other_profiles(self):
        """
        Test inauthented user can not delete any profiles
        """
        self.client.login(username='vicky', password='testpass')
        response = self.client.delete('profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # pass 404 and not 403 ????
