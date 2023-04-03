from rest_framework import serializers
from rest_framework.permissions import AllowAny

from .models import User_snt, SNT


class SNTSerializer(serializers.ModelSerializer):
    class Meta:
        model = SNT
        fields = '__all__'


class User_sntProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_snt
        fields = ['id', 'last_name', 'first_name', 'middle_name', 'email', 'password', 'snt_id']


class User_sntSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_snt
        fields = ['last_name', 'first_name', 'middle_name', 'email']
