from rest_framework import generics, status
from rest_framework.response import Response

from questions.models import Question
from questions.serializers import QuestionSerializer, Question_ALL_Serializer


class QuestionListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filterset_fields = ['meeting_id']

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_object(self):
        return Question.objects.get(id=self.kwargs['id'])


class Question_ALL_ListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = Question_ALL_Serializer
    filterset_fields = ['meeting_id']

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Question_ALL_DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = Question_ALL_Serializer

    def get_object(self):
        return Question.objects.get(id=self.kwargs['id'])
