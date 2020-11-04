from django.db import models
from django.db.models import CharField


class ClientModel(models.Model):
    channel_name = CharField(max_length=255, default="")
