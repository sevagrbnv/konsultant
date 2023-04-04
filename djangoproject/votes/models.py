from django.db import models

from questions.models import Question


class Vote(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='votes')
    type = models.IntegerField(blank=False)
    user_id = models.IntegerField(blank=False)

    def __str__(self):
        return f'{self.id} {self.question_id} {self.type} {self.user_id}'