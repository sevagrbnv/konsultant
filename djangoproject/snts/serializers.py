from rest_framework import serializers

from meetings.serializers import MeetingSerializer, Meeting_ALL_Serializer
from snts.models import SNT
from users.models import User_snt


class SNTSerializer(serializers.ModelSerializer):
    govers = serializers.SerializerMethodField()
    not_govers = serializers.SerializerMethodField()

    def get_govers(self, obj):
        filterargs = {'snt_id': obj.id, 'is_gover': True, 'is_verif': True}
        return User_snt.objects.filter(**filterargs).count()

    def get_not_govers(self, obj):
        filterargs = {'snt_id': obj.id, 'is_gover': False, 'is_verif': True}
        return User_snt.objects.filter(**filterargs).count()

    class Meta:
        model = SNT
        fields = ['id', 'name', 'govers', 'not_govers']


class SNT_ALL_Serializer(serializers.ModelSerializer):
    meetings = Meeting_ALL_Serializer(many=True, read_only=True)

    class Meta:
        model = SNT
        fields = '__all__'
