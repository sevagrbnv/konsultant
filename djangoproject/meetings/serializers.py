from rest_framework import serializers

from docs.serializers import DocSerializer
from meetings.models import Meeting
from questions.serializers import QuestionSerializer


class MeetingSerializer(serializers.ModelSerializer):
    docs = DocSerializer(many=True, read_only=True)
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Meeting
        fields = '__all__'
