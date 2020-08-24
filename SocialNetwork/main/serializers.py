from rest_framework import serializers

from .models import Post, Preference, UserActivity


class userProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserActivity
        fields = '__all__'


class postSerializer(serializers.ModelSerializer):
    post = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class preferenceSerializer(serializers.ModelSerializer):
    preference = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Preference
        fields = '__all__'
