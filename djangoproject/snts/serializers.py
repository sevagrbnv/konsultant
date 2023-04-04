from rest_framework import serializers

from snts.models import SNT


class SNTSerializer(serializers.ModelSerializer):
    class Meta:
        model = SNT
        fields = ['id', 'name']
