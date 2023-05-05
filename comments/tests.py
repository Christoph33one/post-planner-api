from django.contrib.auth.models import User
from .models import TravelPlan
from .models import Comment
from rest_framework import status
from rest_framework.test import APITestCase


class CommentListViewsTest(APITestCase):
    def setUp(self):
        chris = User.objects.create_user(username='chris', password='testpass')
        post = TravelPlan.objects.create(owner=chris, title='great travel plan')

    def test_can_list_comments(self):
        chris = User.objects.get(username='chris')
        post = TravelPlan.objects.get(id=1)
        Comment.objects.create(
            owner=chris, post=post, content='added a comment'
        )
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_out_cant_not_add_comment(self):
        """
        Test logged out user can not add a comment
        """
        post = TravelPlan.objects.get(id=1)
        response = self.client.post(
            '/comments/', {'post': TravelPlan, 'content': 'commenting when logged out'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        count = Comment.objects.count()
        self.assertEqual(count, 0)
        # passed

    def test_logged_in_user_can_add_comment(self):
        """
        Test logged in user can add a comment
        """
        self.client.login(username='chris', password='testpass')
        post = TravelPlan.objects.get(id=1)
        current_user = User.objects.get(username='chris')
        response = self.client.post(
            '/comments/', {
                'owner': current_user, 'post': 1, 'content': 'commenting logged in'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # passed


class CommentDetailListViewTest(APITestCase):
    def setUp(self):
        chris = User.objects.create_user(username='chris', password='testpass')
        brian = User.objects.create_user(username='brian', password='testpass')
        post = TravelPlan.objects.create(owner=chris, title='chris added comment')
        posting = TravelPlan.objects.create(owner=brian, title='brian added comment')
        Comment.objects.create(
            owner=chris, post=post, content='chris has commented'
        )
        Comment.objects.create(
            owner=brian, post=posting, content='brian has commented'
        )

    def test_cant_retreieve_comment_with_invaild_id(self):
        """
        Test can not retreieve comment with incorrect user ID
        """
        response = self.client.get('/comments/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # passes

    def test_can_retrieve_comment_with_vailid_id(self):
        """
        Test can retrieve user comment with matching Id
        """
        response = self.client.get('/comments/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # passes

    def test_logged_in_user_can_update_their_comment(self):
        """
        Test logged in user can update their comment
        """
        self.client.login(username='chris', password='testpass')
        response = self.client.put(
            '/comments/1/', {'content': 'logged in comment'}
        )
        comment = Comment.objects.filter(pk=1).first()
        self.assertEqual(comment.content, 'logged in comment')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_not_update_other_users_comment(self):
        """
        Test user can only update their comment and not other users comments
        """
        self.client.login(username='chris', password='testpass')
        response = self.client.put(
            '/comments/2/', {'content': 'chris edited a comment'}, follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # passes

    def test_user_can_delete_their_comment(self):
        """
        Test user can delete a comment they own
        """
        self.client.login(username='chris', password='testpass')
        response = self.client.delete('/comments/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # passes

    def test_user_can_not_delete_other_user_comment(self):
        """
        Test user can not delete a comment they do not own
        """
        self.client.login(username='brian', password='testpass')
        response = self.client.delete('/comments/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # passes
