from rest_framework import generics

from snts.models import SNT
from snts.serializers import SNTSerializer, SNT_ALL_Serializer


# Create your views here.
class SNTView(generics.ListCreateAPIView):
    queryset = SNT.objects.all()
    serializer_class = SNTSerializer


class ALL(generics.ListAPIView):
    queryset = SNT.objects.all()
    serializer_class = SNT_ALL_Serializer
    filterset_fields = ['id']
