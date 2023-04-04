from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from .models import User_snt, SNT
from .serializers import User_sntSerializer, User_sntProfileSerializer



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
        #user = User_snt.objects.get(email=self.kwargs['email'])
        #password = self.kwargs['password']
        #if (user.password != password):
        #    return User_snt(email="Ошибка", password="Ошибка")
        try:
            user = User_snt.objects.get(email=self.kwargs['email'])
        except User_snt.DoesNotExist:
            user = None
        return user

