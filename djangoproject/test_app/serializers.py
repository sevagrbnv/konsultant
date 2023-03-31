from rest_framework.serializers import ModelSerializer

from test_app.models import Worker


class WorkerSerializer(ModelSerializer):
    class Meta:
        model = Worker
        fields = ['id', 'name', 'second_name', 'salary']

