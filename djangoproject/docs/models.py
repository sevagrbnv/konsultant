from django.db import models

from meetings.models import Meeting


class Doc(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, blank=True)
    meeting_id = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='docs')
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return f'{self.id} {self.name} {self.type} {self.meeting_id}'


class DocTemp(models.Model):
    doc_type = models.CharField(max_length=50)
    meeting_id = models.IntegerField

    def __str__(self):
        return f'{self.id} {self.name} {self.type} {self.meeting_id}'


