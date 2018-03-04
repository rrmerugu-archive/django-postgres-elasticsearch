from django.db import models
from django.utils import timezone


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now())
