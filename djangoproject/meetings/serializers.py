from rest_framework import serializers

from docs.serializers import DocSerializer
from meetings.models import Meeting
from questions.serializers import Question_ALL_Serializer


class MeetingSerializer(serializers.ModelSerializer):
    date_times = serializers.SerializerMethodField()

    def get_date_times(self, obj):
        if (obj.form == 'очной'):
            # {times[0]}-{times[1]} {dates[0]}
            times, date = obj.date.split(' ')
            time1, time2 = times.split('-')
            return {'ochnaya': {'time1': time1, 'time2': time2, 'date': date}}
        elif (obj.form == 'заочной'):
            # {times[0]}-{times[1]} {dates[0]}-{dates[1]}
            times, dates = obj.date.split(' ')
            time1, time2 = times.split('-')
            date1, date2 = dates.split('-')
            return {'zaochnaya': {'time1': time1, 'time2': time2, 'date1': date1, 'date2': date2}}
        else:
            # {times[0]}-{times[1]} {dates[0]} / {times[2]}-{times[3]} {dates[1]}-{dates[2]}
            och, zaoch = obj.date.split(' / ')
            times, date = och.split(' ')
            time1, time2 = times.split('-')

            times, dates = zaoch.split(' ')
            time3, time4 = times.split('-')
            date3, date4 = dates.split('-')

            return {'ochnaya': {'time1': time1, 'time2': time2, 'date': date},
                    'zaochnaya': {'time1': time3, 'time2': time4, 'date1': date3, 'date2': date4}}

    class Meta:
        model = Meeting
        fields = '__all__'


class Meeting_ALL_Serializer(serializers.ModelSerializer):
    docs = DocSerializer(many=True, read_only=True)
    questions = Question_ALL_Serializer(many=True, read_only=True)
    date_times = serializers.SerializerMethodField()

    def get_date_times(self, obj):
        if (obj.form == 'очной'):
            # {times[0]}-{times[1]} {dates[0]}
            times, date = obj.date.split(' ')
            time1, time2 = times.split('-')
            return {'ochnaya': {'time1': time1, 'time2': time2, 'date': date}}
        elif (obj.form == 'заочной'):
            # {times[0]}-{times[1]} {dates[0]}-{dates[1]}
            times, dates = obj.date.split(' ')
            time1, time2 = times.split('-')
            date1, date2 = dates.split('-')
            return {'zaochnaya': {'time1': time1, 'time2': time2, 'date1': date1, 'date2': date2}}
        else:
            # {times[0]}-{times[1]} {dates[0]} / {times[2]}-{times[3]} {dates[1]}-{dates[2]}
            och, zaoch = obj.date.split(' / ')
            times, date = och.split(' ')
            time1, time2 = times.split('-')

            times, dates = zaoch.split(' ')
            time3, time4 = times.split('-')
            date3, date4 = dates.split('-')

            return {'ochnaya': {'time1': time1, 'time2': time2, 'date': date},
                    'zaochnaya': {'time1': time3, 'time2': time4, 'date1': date3, 'date2': date4}}

    class Meta:
        model = Meeting
        fields = '__all__'
