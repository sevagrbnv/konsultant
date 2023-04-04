from rest_framework import generics

from snts.models import SNT
from snts.serializers import SNTSerializer


# Create your views here.
class SNTView(generics.ListCreateAPIView):
    queryset = SNT.objects.all()
    serializer_class = SNTSerializer
