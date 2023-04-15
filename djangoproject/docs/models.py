from django.db import models

from meetings.models import Meeting


class Doc(models.Model):
    meeting_id = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='docs')
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return f'{self.id} {self.meeting_id}'


