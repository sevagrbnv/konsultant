from rest_framework import serializers

from docs.serializers import DocSerializer
from Utils.TimeParser import DateTimeParser
from meetings.models import Meeting
from questions.serializers import Question_ALL_Serializer


class MeetingSerializer(serializers.ModelSerializer):
    date_times = serializers.SerializerMethodField()

    def get_date_times(self, obj):
        datetimeParser = DateTimeParser()
        return datetimeParser.toDict(string=obj.date, form=obj.form)

    class Meta:
        model = Meeting
        fields = '__all__'


class Meeting_ALL_Serializer(serializers.ModelSerializer):
    docs = DocSerializer(many=True, read_only=True)
    questions = Question_ALL_Serializer(many=True, read_only=True)
    date_times = serializers.SerializerMethodField()

    def get_date_times(self, obj):
        datetimeParser = DateTimeParser()
        return datetimeParser.toDict(string=obj.date, form=obj.form)

    class Meta:
        model = Meeting
        fields = '__all__'
