import os
import tempfile
import zipfile

from django.http import FileResponse, Http404, HttpResponse
from rest_framework import generics, views
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
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        file_obj = request.FILES['file']
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


class DocDownloadView(views.APIView):
    def get(self, request, meeting_id):
        # Получить все объекты Doc с заданным meeting_id.
        docs = Doc.objects.filter(meeting_id=meeting_id)

        # Создать временный каталог для сохранения файлов.
        with tempfile.TemporaryDirectory() as temp_dir:
            # Сохранить все файлы, связанные с объектами Doc, во временный каталог.
            for doc in docs:
                file_path = doc.file.path
                file_name = doc.file.name.split('/')[-1]
                with open(file_path, 'rb') as f:
                    with open(f'{temp_dir}/{file_name}', 'wb') as temp_f:
                        temp_f.write(f.read())

            # Создать временный файл для записи архива.
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                # Создать архив из всех файлов, сохраненных во временном каталоге.
                with zipfile.ZipFile(temp_file, 'w') as zip_f:
                    for file_name in os.listdir(temp_dir):
                        zip_f.write(f'{temp_dir}/{file_name}', file_name)

            # Создать HTTP-ответ, который содержит ссылку на временный файл.
            response = HttpResponse(content_type='application/zip')
            response['Content-Disposition'] = f'attachment; filename=docs.zip'
            with open(temp_file.name, 'rb') as f:
                response.write(f.read())

            # Удалить временный файл.
            os.unlink(temp_file.name)

            return response