from rest_framework import serializers

from meetings.serializers import MeetingSerializer
from snts.models import SNT


class SNTSerializer(serializers.ModelSerializer):
    meetings = MeetingSerializer(many=True, read_only=True)

    class Meta:
        model = SNT
        fields = '__all__'

