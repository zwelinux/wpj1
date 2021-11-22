from django.db import models

# Create your models here.
class Record(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField()

