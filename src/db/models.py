from django.db import models


class JsonReceivedModel(models.Model):
    userId = models.CharField(max_length=100)
    jsonId = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    completed = models.CharField(max_length=100)
