from .models import Task


class TaskService():
    def __str__(self):
        return 'TaskService'

    def create(self, title, text):
        try:
            task = Task(title=title, text=text)
            task.save()
        except:
            return False
        else:
            return True

    def delete(self, id):
        try:
            task = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return False
        else:
            task.delete()
            return True

    def get_last_by_id(self):
        return Task.objects.latest('id').id

    def order_by_descending(self):
        return Task.objects.order_by('-id')
