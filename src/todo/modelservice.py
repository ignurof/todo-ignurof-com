from .models import Task


class TaskService():
    def __str__(self):
        return 'TaskService'

    def create_task(self, title, text):
        task = Task(title=title, text=text)
        task.save()
