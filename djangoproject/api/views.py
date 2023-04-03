from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User_snt, SNT
from .serializers import User_sntSerializer, SNTSerializer, User_sntProfileSerializer


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
        user = User_snt.objects.get(email=self.kwargs['email'])
        password = self.kwargs['password']
        if (user.password != password):
            return Response( status=status.HTTP_400_BAD_REQUEST)
        return user


#class UserDetailView(APIView):

#    def get_object(self):
#        try:
#            return User_snt.objects.get(first_name=self.kwargs['first_name'])
#        except User_snt.DoesNotExist:
#            raise Http404

#    def get(self, request, pk):
#        snippet = self.get_object(pk)
#        serializer = User_sntProfileSerializer(snippet)
#        return Response(serializer.data)

#    def put(self, request, pk):
#        snippet = self.get_object(pk)
#        serializer = User_sntProfileSerializer(snippet, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#    def delete(self, request, pk):
#        snippet = self.get_object(pk)
#        snippet.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
