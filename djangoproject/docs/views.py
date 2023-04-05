from django.http import FileResponse, Http404
from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from docs.models import Doc
from docs.serializers import DocSerializer
from meetings.models import Meeting


class DocListView(generics.ListCreateAPIView):
    queryset = Doc.objects.all().order_by('-id')
    serializer_class = DocSerializer
    filterset_fields = ['meeting_id']

class DocDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer

    def get_object(self):
        return Doc.objects.get(id=self.kwargs['id'])


class FileUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        file_obj = request.data['file']
        name = request.data['name']
        type = request.data['type']
        meeting_id = int(request.data['meeting_id'])
        meeting = Meeting.objects.get(pk=meeting_id)
        my_model = Doc(name=name, type=type, meeting_id=meeting, file=file_obj)
        my_model.save()
        return Response({'message': 'File created', 'id': my_model.id})


class FileDownloadView(APIView):
    def get(self, request, pk, format=None):
        try:
            my_model = Doc.objects.get(id=pk)
            file_path = my_model.file.path
            response = FileResponse(open(file_path, 'rb'))
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(my_model.file.name)
            return response
        except Doc.DoesNotExist:
            raise Http404
