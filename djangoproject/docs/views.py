import os
import tempfile
import zipfile
from datetime import datetime

from django.core.files import File
from django.core.files.base import ContentFile
from django.http import FileResponse, Http404
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from Utils.BulletinCreator import create_bulletin
from Utils.DecisionCreator import create_decision
from Utils.NotificationCretor import create_notification
from Utils.ProtocolCreator import create_protocol
from Utils.VoteCounter import voteCount
from docs.models import Doc
from docs.serializers import DocSerializer
from Utils.ProtocolParser import ProtocolParser
from meetings.models import Meeting
from questions.models import Question
from questions.serializers import QuestionSerializer


class DocListView(generics.ListCreateAPIView):
    queryset = Doc.objects.all().order_by('-id')
    serializer_class = DocSerializer
    filterset_fields = ['meeting_id']


class DocDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer

    def get_object(self):
        return Doc.objects.get(id=self.kwargs['id'])


# Загрузка на сервер
class FileUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        file_obj = request.data['file']
        meeting_id = int(request.data['meeting_id'])
        meeting = Meeting.objects.get(pk=meeting_id)
        my_model = Doc(meeting_id=meeting, file=file_obj)
        my_model.save()

        doc = ProtocolParser(my_model.file.path)
        protocol_date = doc.get_protocol_creating_date()
        dates = doc.get_list_of_dates()
        times = doc.get_list_of_times()
        form = doc.get_form()
        type = doc.get_type()
        place = doc.get_place(form=form)
        questions = doc.get_questions()
        string_date = doc.format_datetime(form=form, dates=dates, times=times)

        meeting.date = string_date
        meeting.protocol_date = protocol_date
        meeting.place = place
        meeting.type = type
        meeting.form = form
        meeting.save()

        for parsed_question in questions:
            questModel = Question(meeting_id=meeting, question=parsed_question)
            questModel.save()

        current_date = datetime.today().strftime('%d.%m.%Y')
        bulletin = create_bulletin('doc_templates/bulleten_form.docx', type, meeting.date, form, questions)
        notification = create_notification('doc_templates/notification_form.docx', type, string_date, form, questions,
                                           protocol_date,
                                           current_date + 'г.')

        with open(f'./uploads/{bulletin}', 'rb') as f:
            file_data = f.read()
        django_file = ContentFile(file_data)
        my_file = File(file_data)
        my_model = Doc(meeting_id=meeting)
        my_model.file.save(f'Бюллетень_{meeting_id}.docx', django_file)
        my_model.save()

        with open(f'./uploads/{notification}', 'rb') as f:
            file_data = f.read()
        django_file = ContentFile(file_data)
        my_file = File(file_data)
        my_model = Doc(meeting_id=meeting)
        my_model.file.save(f'Уведомление_{meeting_id}.docx', django_file)
        my_model.save()

        return Response({'message': 'Files created', 'meeting_id': meeting_id, 'questions': questions})


# Скачивание одного документа
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


# Скачивание архива по meeting_id
class ZipDownloadView(APIView):
    def get(self, request, meeting_id):
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


class DecisionDataView(APIView):
    def post(self, request, format=None):
        questions_data = request.data
        serializer = QuestionSerializer(data=questions_data, many=True)
        if serializer.is_valid():

            questions = [Question(**item) for item in serializer.validated_data]
            questModels = Question.objects.filter(meeting_id=questions[0].meeting_id)
            meeting = Meeting.objects.get(id=questions[0].meeting_id.id)

            for i in range(len(questModels)):
                questModels[i].decision = questions[i].decision
                questModels[i].yes = questions[i].yes
                questModels[i].no = questions[i].no
                questModels[i].idk = questions[i].idk
                questModels[i].save()

            zaoch_list = []
            for quest in questModels:
                list = [voteCount(quest, 1), voteCount(quest, 0), voteCount(quest, -1)]
                zaoch_list.append(list)

            current_date = datetime.today().strftime('%d.%m.%Y')
            protocol = create_protocol('./doc_templates/protocol_form.docx', meeting.type, meeting.date,
                                       meeting.form, questModels, zaoch_list,
                                       meeting.protocol_date,
                                       current_date)

            decision = create_decision('./doc_templates/solution_form.docx', meeting.type, meeting.date, meeting.form,
                                       questModels, zaoch_list, meeting.protocol_date, current_date)

            with open(f'./uploads/{protocol}', 'rb') as f:
                file_data = f.read()
            django_file = ContentFile(file_data)
            my_file = File(file_data)
            my_model = Doc(meeting_id=meeting)
            my_model.file.save(f'Протокол_собрания_{meeting.id}.docx', django_file)
            my_model.save()

            with open(f'./uploads/{decision}', 'rb') as f:
                file_data = f.read()
            django_file = ContentFile(file_data)
            my_file = File(file_data)
            my_model = Doc(meeting_id=meeting)
            my_model.file.save(f'Решение_{meeting.id}.docx', django_file)
            my_model.save()

            os.remove(f'./uploads/{decision}')
            os.remove(f'./uploads/{protocol}')

            return Response("Success", status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
