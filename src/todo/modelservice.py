from .models import Task


class TaskService:
    def __str__(self):
        return "TaskService"

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
            return {"error_code": 1, "message": "Task not found"}
        else:
            task.delete()
            return {"error_code": 0, "message": "Deleted Task(%i)" % id}

    def get_last_by_id(self):
        return Task.objects.latest("id").id

    def order_by_descending(self):
        return Task.objects.order_by("-id")
