from django.db import models
import datetime


class Task(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100)
    priority=models.IntegerField()
    date=models.DateField(default=datetime.date.today)


