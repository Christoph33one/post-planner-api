from django.db import models
from profiles.models import Profile
from django.contrib.auth.models import User


class TravelPlan(models.Model):
    image_filter_choices = [
        ('_1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=500, blank=False)
    location = models.CharField(max_length=100, blank=False)
    activities = models.CharField(max_length=80, choices=Profile.ACTIVITY_CHOICES, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../https://res.cloudinary.com/dqgs0kltd/image/upload/v1673026764/samples/ecommerce/accessories-bag.jpg', blank=True
    )
    approved = models.BooleanField(default=False)

    image_filter = models.CharField(
        max_length=40, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
