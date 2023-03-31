from rest_framework.serializers import ModelSerializer

from login.models import SNT, User_snt


class SntSerializer(ModelSerializer):
    class Meta:
        model = SNT
        fields = ['id', 'name', 'description', 'address']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User_snt
        fields = [
            'id',
            'firstname',
            'lastname',
            'middlename',
            'email',
            'phone',
            'hash_pass',
            'snt_id',
            'address',
            'is_admin',
            'is_verif',
            'is_gover'
        ]
