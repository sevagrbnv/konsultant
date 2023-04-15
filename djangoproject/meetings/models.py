from django.db import models
from snts.models import SNT


class Meeting(models.Model):
    protocol_date = models.CharField(max_length=20, blank=True)
    date = models.CharField(max_length=100, blank=True)
    place = models.CharField(max_length=100, blank=True)
    snt_id = models.ForeignKey(SNT, on_delete=models.CASCADE, related_name='meetings')
    type = models.CharField(max_length=100, blank=True)
    form = models.CharField(max_length=100, blank=True)
    is_solved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.date} {self.place}'
