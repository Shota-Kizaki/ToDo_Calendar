from django.db import models

class ToDo(models.Model):
    event_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    memo = models.TextField()
    situation = models.CharField(max_length=10, choices=[('未着手', '未着手'), ('進行中', '進行中'), ('完了', '完了')])

    def __str__(self):
        return self.event_name
