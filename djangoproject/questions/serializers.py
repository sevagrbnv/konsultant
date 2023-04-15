from rest_framework import serializers

from Utils.VoteCounter import voteCount
from questions.models import Question
from votes.serializers import VoteSerializer


class QuestionSerializer(serializers.ModelSerializer):
    zaoch_yes = serializers.SerializerMethodField()
    zaoch_no = serializers.SerializerMethodField()
    zaoch_idk = serializers.SerializerMethodField()

    def get_zaoch_yes(self, obj):
        return voteCount(obj=obj, type=1)

    def get_zaoch_no(self, obj):
        return voteCount(obj=obj, type=-1)

    def get_zaoch_idk(self, obj):
        return voteCount(obj=obj, type=0)

    class Meta:
        model = Question
        fields = '__all__'


class Question_ALL_Serializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'
