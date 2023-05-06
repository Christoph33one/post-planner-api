from rest_framework import serializers
from .models import TravelPlan


class TravelPlanSerializer(serializers.ModelSerializer):
    """
    Serializes TravelPlan model data into a specific format
    for storage or transmission.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger that 4096px'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = TravelPlan
        fields = [
            'id'
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'created_at',
            'title',
            'description',
            'location',
            'activities',
            'caption',
            'image1',
            'image2',
            'image3',
            'image4',
            'image5',
            'image6',
            'image_filter',
            'comments_count'
        ]
