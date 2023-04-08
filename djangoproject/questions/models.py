from django.db import models

from meetings.models import Meeting


class Question(models.Model):
    meeting_id = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='questions')
    question = models.CharField(max_length=256, blank=False)
    yes = models.IntegerField(default=0)
    no = models.IntegerField(default=0)
    idk = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.id} {self.question} {self.meeting_id}\n {self.yes}/{self.no}/{self.idk}'
