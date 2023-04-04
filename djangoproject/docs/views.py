from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from docs.models import Doc
from docs.serializers import DocSerializer


class DocListView(generics.ListCreateAPIView):
    queryset = Doc.objects.all().order_by('-id')
    serializer_class = DocSerializer
    filterset_fields = ['meeting_id']

    def post(self, request, format=None):
        serializer = DocSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer

    def get_object(self):
        return Doc.objects.get(id=self.kwargs['id'])
