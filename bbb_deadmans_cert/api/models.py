from django.db import models
from django.db.models import IntegerField, ForeignKey, DateTimeField


class MeetingModel(models.Model):
    meeting_id = IntegerField(default=-1)
    start_time = DateTimeField()
    stop_time = DateTimeField()


class DeadmanStatusModel(models.Model):
    client_id = IntegerField(default=-1)
    meeting = ForeignKey(MeetingModel, on_delete=models.CASCADE)
