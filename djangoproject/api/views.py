from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from .models import User_snt, SNT, Meeting
from .serializers import User_sntSerializer, SNTSerializer, User_sntProfileSerializer, MeetingSerializer


class SNTViewView(generics.ListCreateAPIView):
    queryset = SNT.objects.all()
    serializer_class = SNTSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = User_snt.objects.all()
    serializer_class = User_sntSerializer
    filterset_fields = ['snt_id']

    def post(self, request, format=None):
        serializer = User_sntProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User_snt.objects.all()
    serializer_class = User_sntProfileSerializer

    def get_object(self):
        try:
            user = User_snt.objects.get(email=self.kwargs['email'])
        except User_snt.DoesNotExist:
            user = None
        return user


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
