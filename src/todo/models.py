from django.db import models


class Task(models.Model):
    def __init__(self):
        print('init Task model')

    def __str__(self):
        return self.title

    title = models.CharField(max_length=20)
    text = models.CharField(max_length=120)
