from rest_framework import serializers

from meetings.serializers import MeetingSerializer, Meeting_ALL_Serializer
from snts.models import SNT


class SNTSerializer(serializers.ModelSerializer):

    class Meta:
        model = SNT
        fields = ['id', 'name']


class SNT_ALL_Serializer(serializers.ModelSerializer):
    meetings = Meeting_ALL_Serializer(many=True, read_only=True)

    class Meta:
        model = SNT
        fields = '__all__'
