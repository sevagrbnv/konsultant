from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from questions.models import Question
from votes.models import Vote
from .models import User_snt, SNT
from .serializers import UserSerializer, UserProfileSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = User_snt.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['snt_id']

    def post(self, request, format=None):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User_snt.objects.all()
    serializer_class = UserProfileSerializer

    def get_object(self):
        try:
            user = User_snt.objects.get(email=self.kwargs['email'])
        except User_snt.DoesNotExist:
            user = None
        return user


class VotedUserListView(generics.ListCreateAPIView):
    queryset = User_snt.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        meeting_id = request.query_params.get('meeting_id')
        questions = Question.objects.filter(meeting_id=meeting_id)
        votes = Vote.objects.filter(question_id=questions[0].id).all()
        user_list = []
        for vote in votes:
            user = User_snt.objects.get(id=vote.user_id)
            user_list.append(user)
        serializer = self.serializer_class(user_list, many=True)
        return Response(serializer.data)
