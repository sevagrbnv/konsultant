import os
import tempfile
import zipfile

from django.core.files.base import ContentFile
from django.http import FileResponse, Http404
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from docs.models import Doc
from docs.serializers import DocSerializer, NotificationSerializer, BulletinSerializer, MeetingProtocolSerializer, \
    DecisionSerializer
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
            model = Doc.objects.get(id=pk)
            file_path = model.file.path
            response = FileResponse(open(file_path, 'rb'))
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(model.file.name)
            return response
        except Doc.DoesNotExist:
            raise Http404


class ZipDownloadView(APIView):
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


class DocCreateView(generics.CreateAPIView):
    queryset = Doc.objects.all()
    serializer_class = None

    def post(self, request, *args, **kwargs):
        meeting_id = request.data.get('meeting_id')
        doc_type = request.data.get('doc_type')

        if not meeting_id or not doc_type:
            return Response(
                {'error': 'meeting_id and doc_type are required fields'},
                status=status.HTTP_400_BAD_REQUEST
            )
        meeting = Meeting.objects.filter(id=meeting_id).first()

        if not meeting:
            return Response(
                {'error': f'Meeting with id={meeting_id} not found'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if doc_type == 'Уведомление':
            serializer_class = NotificationSerializer
            doc_template = 'doc_templates/notification.docx'
        elif doc_type == 'Бюллетень':
            serializer_class = BulletinSerializer
            doc_template = 'doc_templates/bulletin.docx'
        elif doc_type == 'ПротоколСобрания':
            serializer_class = MeetingProtocolSerializer
            doc_template = 'doc_templates/protocol.docx'
        elif doc_type == 'Решение':
            serializer_class = DecisionSerializer
            doc_template = 'doc_templates/decision.docx'
        else:
            return Response(
                {'error': f'Document type "{doc_type}" is not supported'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        with open(doc_template, 'rb') as file:
            file_data = file.read()
        django_file = ContentFile(file_data)

        doc = Doc(name=doc_type + '_' + meeting_id,
                  type=doc_type,
                  meeting_id=meeting)
        doc.file.save(f'{doc_type}_{meeting_id}.docx', django_file)
        doc.save()

        # Return the serialized data of the created document
        return Response({
            "data": "Success",
            "id": doc.id
        }, status=status.HTTP_201_CREATED)
