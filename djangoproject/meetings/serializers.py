from rest_framework import serializers

from docs.serializers import DocSerializer
from meetings.models import Meeting
from questions.serializers import QuestionSerializer, Question_ALL_Serializer


class MeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting
        fields = '__all__'


class Meeting_ALL_Serializer(serializers.ModelSerializer):
    docs = DocSerializer(many=True, read_only=True)
    questions = Question_ALL_Serializer(many=True, read_only=True)

    class Meta:
        model = Meeting
        fields = '__all__'
