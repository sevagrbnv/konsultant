from rest_framework import serializers

from .models import User_snt, SNT, Meeting


class SNTSerializer(serializers.ModelSerializer):
    class Meta:
        model = SNT
        fields = ['id', 'name']


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ['id', 'date', 'time', 'snt_id', 'place', 'type']


class User_sntProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_snt
        fields = ['id', 'last_name', 'first_name', 'middle_name', 'email', 'password', 'snt_id',
                  'is_verif', 'is_gover', 'is_admin']


class User_sntSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_snt
        fields = ['last_name', 'first_name', 'middle_name', 'email']
