from rest_framework import serializers

from questions.models import Question
from votes.serializers import VoteSerializer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class Question_ALL_Serializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'
