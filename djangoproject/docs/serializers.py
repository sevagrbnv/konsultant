from rest_framework import serializers

from docs.models import Doc


class DocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doc
        fields = ['id', 'name', 'type', 'path', 'meeting_id']
