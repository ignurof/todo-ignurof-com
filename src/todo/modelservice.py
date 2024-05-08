from .models import Task


class TaskService():
    def __str__(self):
        return 'TaskService'

    def create_task(self, title, text):
        task = Task(title=title, text=text)
        task.save()

    def delete_task(self, id):
        try:
            task = Task.objects.get(id=id)
        except(ObjectDoesNotExist):
            return False
        else:
            task.delete()
            return True

    def order_by_descending(self):
        return Task.objects.order_by('-id')
