from django.db import models

from meetings.models import Meeting


class Doc(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, blank=True)
    path = models.CharField(max_length=256, blank=True)
    meeting_id = models.ForeignKey(Meeting, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.name} {self.type} {self.meeting_id}'
