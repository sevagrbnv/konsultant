from rest_framework import generics, status
from rest_framework.response import Response
from meetings.models import Meeting
from meetings.serializers import MeetingSerializer, Meeting_ALL_Serializer


class MeetingListView(generics.ListCreateAPIView):
    queryset = Meeting.objects.all().order_by('-date')
    serializer_class = MeetingSerializer
    filterset_fields = ['snt_id']

    def post(self, request, format=None):
        serializer = MeetingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeetingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def get_object(self):
        return Meeting.objects.get(id=self.kwargs['id'])


class Meeting_ALL_ListView(generics.ListCreateAPIView):
    queryset = Meeting.objects.all().order_by('-date')
    serializer_class = Meeting_ALL_Serializer
    filterset_fields = ['snt_id']

    def post(self, request, format=None):
        serializer = MeetingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Meeting_ALL_DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = Meeting_ALL_Serializer

    def get_object(self):
        return Meeting.objects.get(id=self.kwargs['id'])
