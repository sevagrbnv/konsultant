from rest_framework import serializers
from rest_framework.reverse import reverse

from docs.models import Doc


class DocSerializer(serializers.ModelSerializer):
    download_link = serializers.SerializerMethodField()

    def get_download_link(self, obj):
        request = self.context.get('request')
        meeting_id = obj.meeting_id.id
        url = request.build_absolute_uri(reverse('doc-download', args=[obj.meeting_id.id]))
        return url

    class Meta:
        model = Doc
        fields = ['id', 'name', 'meeting_id', 'download_link']

