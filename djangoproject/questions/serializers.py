from rest_framework import serializers

from questions.models import Question
from votes.serializers import VoteSerializer


class QuestionSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'
