from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    note = models.TextField()  # Actual note
