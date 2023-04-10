from rest_framework import serializers
from rest_framework.reverse import reverse
from docs.models import Doc, DocTemp


class DocSerializer(serializers.ModelSerializer):
    download_link = serializers.SerializerMethodField()

    def get_download_link(self, obj):
        request = self.context.get('request')
        meeting_id = obj.meeting_id.id
        url = request.build_absolute_uri(reverse('zip-download', args=[obj.meeting_id.id]))
        return url

    class Meta:
        model = Doc
        fields = ['id', 'name', 'meeting_id', 'download_link']


# Уведомление, Бюллетень, Протокол Правления, Протокол собрания и Решение
class NotificationSerializer(serializers.ModelSerializer):
    # field1 = serializers.CharField()
    # field2 = serializers.IntegerField()
    # field3 = serializers.DateField()

    class Meta:
        model = DocTemp
        fields = '__all__'


class BulletinSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocTemp
        fields = '__all__'


class MeetingProtocolSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocTemp
        fields = '__all__'


class DecisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocTemp
        fields = '__all__'
