from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from votes.models import Vote
from votes.serializers import VoteSerializer


class VoteListView(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    filterset_fields = ['question_id']

    def post(self, request, format=None):
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def get_object(self):
        return Vote.objects.get(id=self.kwargs['id'])
