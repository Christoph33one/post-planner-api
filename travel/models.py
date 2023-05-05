from django.db import models
from profiles.models import Profile
from django.contrib.auth.models import User


class TravelPlan(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=500, blank=False)
    location = models.CharField(max_length=100, blank=False)
    activities = models.CharField(
        max_length=80, choices=Profile.ACTIVITY_CHOICES, blank=True)
    approved = models.BooleanField(default=False)

    image1 = models.ImageField(
        upload_to='images/', default='../https://res.cloudinary.com/dqgs0kltd/image/upload/v1673026764/samples/ecommerce/accessories-bag.jpg', blank=True)
    image2 = models.ImageField(
        upload_to='images/', default='../https://res.cloudinary.com/dqgs0kltd/image/upload/v1673026764/samples/ecommerce/accessories-bag.jpg', blank=True)
    image3 = models.ImageField(
        upload_to='images/', default='../https://res.cloudinary.com/dqgs0kltd/image/upload/v1673026764/samples/ecommerce/accessories-bag.jpg', blank=True)
    image4 = models.ImageField(
        upload_to='images/', default='../https://res.cloudinary.com/dqgs0kltd/image/upload/v1673026764/samples/ecommerce/accessories-bag.jpg', blank=True)
    image5 = models.ImageField(
        upload_to='images/', default='../https://res.cloudinary.com/dqgs0kltd/image/upload/v1673026764/samples/ecommerce/accessories-bag.jpg', blank=True)
    image6 = models.ImageField(
        upload_to='images/', default='../https://res.cloudinary.com/dqgs0kltd/image/upload/v1673026764/samples/ecommerce/accessories-bag.jpg', blank=True)

    image_filter = models.CharField(
        max_length=50, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
