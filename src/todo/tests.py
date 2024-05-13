from django.test import TestCase
from .modelservice import TaskService


class TestTaskService(TestCase):
    def create_test_task(self):
        return TaskService().create("title", "text")

    def test_create(self):
        created_task = self.create_test_task()
        self.assertEqual(created_task["error_code"], 0)

    def test_delete(self):
        self.create_test_task()
        deleted_task = TaskService().delete(TaskService().get_last_by_id())
        self.assertEqual(deleted_task["error_code"], 0)

    def test_edit(self):
        self.create_test_task()
        edited_task = TaskService().edit(
            TaskService().get_last_by_id(), "title", "text"
        )
        self.assertEqual(edited_task["error_code"], 0)

    def test_get_last_by_id(self):
        self.create_test_task()
        task = TaskService().get_last_by_id()
        self.assertEqual(task, type(task) == int)

    def test_order_by_descending(self):
        self.create_test_task()
        self.create_test_task()
        tasks = TaskService().order_by_descending()
        self.assertEqual(tasks.count(), 2)
