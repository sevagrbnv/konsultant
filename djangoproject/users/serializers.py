from rest_framework import serializers

from .models import User_snt


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_snt
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_snt
        fields = ['id', 'last_name', 'first_name', 'middle_name', 'email', 'phone']
