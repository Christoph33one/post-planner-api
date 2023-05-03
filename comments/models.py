from django.db import models
from django.contrib.auth.models import User
from travel.models import TravelPlan


class Comment(models.Model):
    """
    Comment model, realted to the User and Travel plan
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(TravelPlan, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
