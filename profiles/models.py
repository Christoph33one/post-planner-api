from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


# profile
class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(max_length=200, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_alsdm3.jpg'
    )
    ACTIVITY_CHOICES = (
        ('HIKING', 'Hiking'),
        ('SNOWBOARDIND', 'Snowboarding'),
        ('CYCLING', 'Cycling'),
        ('MOUNTAIN BIKING', 'Mountain biking'),
        ('SWIMMING', 'Swimming'),
        ('CAMPING', 'Camping'),
        ('ROAD TRIPS', 'Road trips'),
        ('EXPLORING', 'Exploring'),
        ('PHOTOGRAPHY', 'Photography'),
    )
    activities = models.CharField(max_length=20, choices=ACTIVITY_CHOICES, blank=True)  # noqa
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
