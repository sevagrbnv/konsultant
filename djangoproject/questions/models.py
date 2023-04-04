from django.db import models

from meetings.models import Meeting


class Question(models.Model):
    time = models.CharField(max_length=10)
    meeting_id = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    question = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.time} {self.date} {self.place}'