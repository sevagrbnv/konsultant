from django.db import models

from snts.models import SNT


class Meeting(models.Model):
    time = models.CharField(max_length=10)
    date = models.CharField(max_length=10)
    place = models.CharField(max_length=100)
    snt_id = models.ForeignKey(SNT, on_delete=models.CASCADE, related_name='meetings')
    type = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.time} {self.date} {self.place}'
