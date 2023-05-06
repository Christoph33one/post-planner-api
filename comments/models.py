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
    content = models.TextField(max_length=250, blank=False)
    comment_image = models.ImageField(
        upload_to='images/',
        default='../https://res.cloudinary.com/dqgs0kltd/image/upload/v1673026764/samples/ecommerce/accessories-bag.jpg',
        blank=True
         )
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
