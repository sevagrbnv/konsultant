from rest_framework import serializers

from questions.models import Question
from votes.models import Vote
from votes.serializers import VoteSerializer


class QuestionSerializer(serializers.ModelSerializer):
    zaoch_yes = serializers.SerializerMethodField()
    zaoch_no = serializers.SerializerMethodField()
    zaoch_idk = serializers.SerializerMethodField()

    def get_zaoch_yes(self, obj):
        filterargs = {'question_id': obj.id, 'type': 0}
        return Vote.objects.filter(**filterargs).count()

    def get_zaoch_no(self, obj):
        filterargs = {'question_id': obj.id, 'type': 1}
        return Vote.objects.filter(**filterargs).count()

    def get_zaoch_idk(self, obj):
        filterargs = {'question_id': obj.id, 'type': 2}
        return Vote.objects.filter(**filterargs).count()

    class Meta:
        model = Question
        fields = '__all__'


class Question_ALL_Serializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'
